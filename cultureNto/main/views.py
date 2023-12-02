import datetime

import django.contrib.admin.sites
from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django_tables2 import RequestConfig
from .models import Event, Work, WorkType, Room, Booking, EventLocation
from .tables import EventTable, RoomTable
from django_tables2.export.export import TableExport
import json
from django.views.decorators.csrf import csrf_exempt


def base(request):
    data = {
        "title": "Главная Страница",
        "header_text": "Главная страница"
    }
    return render(request, "main/base.html", data)


def index(request):
    data = {
        "title": "Главная Страница",
        "header_text": "Главная страница"
    }
    # return redirect("razvlech")
    return render(request, "main/index.html", data)


def tableRender(request):
    sl = {
        "enlightenment": "Просвещение",
        "entertainment": "Развлечения",
        "education": "Образование"
    }
    if "enlightenment" in request.path:
        cat = sl["enlightenment"]
    elif "entertainment" in request.path:
        cat = sl["entertainment"]
    else:
        cat = sl["education"]

    data = {
        "title": f"Страница {cat}",
        "header_text": f"Страница {cat}",
        "cat": cat
    }

    if "enlightenment" in request.path or "entertainment" in request.path:
        table = EventTable(Event.objects.all())
        RequestConfig(request, paginate={"per_page": 2}).configure(table)
        export_format = request.GET.get("_export", None)
        if TableExport.is_valid_format(export_format):
            exporter = TableExport(export_format, table)
            return exporter.response(f"table.{export_format}")
        data["table"] = table
    tableRoom = RoomTable(Room.objects.all())
    RequestConfig(request, paginate={"per_page": 8}).configure(tableRoom)
    data["rooms"] = tableRoom
    return render(request, "main/category_page.html", data)


def roomsRender(request):
    data = {
        "title": f"Страница Помещений",
        "header_text": f"Страница Помещений",
    }
    table = RoomTable(Room.objects.all())
    RequestConfig(request, paginate={"per_page": 8}).configure(table)
    export_format = request.GET.get("_export", None)
    if TableExport.is_valid_format(export_format):
        exporter = TableExport(export_format, table)
        return exporter.response(f"table.{export_format}")
    data["table"] = table
    return render(request, "main/rooms.html", data)


def worktable(request):
    if request.GET.get("del", None) is not None and Work.objects.filter(pk=request.GET.get("del", None)).exists():
        work_obj = Work.objects.get(pk=request.GET.get("del", None))
        work_obj.status = "Выполнена"
        work_obj.save()
    work_type = request.GET.get('select', "all")
    obj = []
    if work_type == "all":
        obj = Work.objects.filter(status="К выполнению")
    else:
        if WorkType.objects.filter(name=work_type).exists():
            obj = Work.objects.filter(work_type=WorkType.objects.get(name=work_type), status="К выполнению")
    data = {'title': "Рабочий стол для заявок", "header_text": "Рабочий стол для заявок", "objects": obj, "workTypes": WorkType.objects.all()}
    return render(request, "main/worktable.html", data)


def start_workers_page(request):
    data = {
        'title': "Страница для сотрудников",
        "header_text": "Страница для сотрудников",
    }
    return render(request, "main/workers.html", data)


def events(request):
    ev = Event.objects.all()
    data = {
        'title': "Мероприятия",
        "header_text": "Страница Мероприятия",
        "events": ev
    }
    return render(request, "main/events.html", data)


def page_brone(request):
    data = {
        "title": "Страница бронирования"
    }
    return render(request, "main/admin_page.html", data)


@csrf_exempt
def get_booking_intersection(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        start_date = datetime.datetime.strptime(json_data["start_date"], "%Y-%m-%d").date()
        start_time = datetime.datetime.strptime(json_data["start_time"], "%H:%M").time()
        end_date = datetime.datetime.strptime(json_data["end_date"], "%Y-%m-%d").date()
        end_time = datetime.datetime.strptime(json_data["end_time"], "%H:%M").time()
        locations_pk = list(map(int, json_data["locations_pk"]))

        start_datetime = datetime.datetime.combine(start_date, start_time)
        end_datetime = datetime.datetime.combine(end_date, end_time)

        intersection = Booking.get_booking_intersection(locations_pk, start_datetime, end_datetime)

        return JsonResponse([
            {
                "description": b.event.description,
                "date_start": b.date_start.strftime("%d.%m.%Y %H:%M"),
                "date_end": b.date_end.strftime("%d.%m.%Y %H:%M")
            }
            for b in intersection
        ], safe=False)
    return HttpResponse("invalid request")


@csrf_exempt
def get_available_rooms(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)

        start_date = datetime.datetime.strptime(json_data["start_date"], "%Y-%m-%d").date()
        start_time = datetime.datetime.strptime(json_data["start_time"], "%H:%M").time()
        end_date = datetime.datetime.strptime(json_data["end_date"], "%Y-%m-%d").date()
        end_time = datetime.datetime.strptime(json_data["end_time"], "%H:%M").time()

        start_datetime = datetime.datetime.combine(start_date, start_time)
        end_datetime = datetime.datetime.combine(end_date, end_time)

        bookings = Booking.objects.exclude(Q(date_end__lt=start_datetime) | Q(date_start__gt=end_datetime))
        unavailable_event_locations = []
        for booking in bookings:
            unavailable_event_locations.extend([l.id for l in booking.locations.all()])

        event_locations = EventLocation.objects.exclude(id__in=unavailable_event_locations)
        rooms = {}
        for event_location in event_locations:
            obj = rooms.get(event_location.room.first().id, {"name": event_location.room.first().name, "locations": []})
            obj["locations"].append({"id": event_location.id, "name": event_location.name})
            rooms[event_location.room.first().id] = obj

        return JsonResponse(rooms, safe=False)
    return HttpResponse("invalid request")


@csrf_exempt
def add_booking(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        start_date = datetime.datetime.strptime(json_data["start_date"], "%Y-%m-%d").date()
        start_time = datetime.datetime.strptime(json_data["start_time"], "%H:%M").time()
        end_date = datetime.datetime.strptime(json_data["end_date"], "%Y-%m-%d").date()
        end_time = datetime.datetime.strptime(json_data["end_time"], "%H:%M").time()
        event_pk = int(json_data["event_pk"])
        locations_pk = list(map(int, json_data["locations_pk"]))
        comment = json_data["comment"]

        start_datetime = datetime.datetime.combine(start_date, start_time)
        end_datetime = datetime.datetime.combine(end_date, end_time)

        booking = Booking(
            date_create=datetime.datetime.now(),
            event=Event.objects.get(id=event_pk),
            date_start=start_datetime,
            date_end=end_datetime,
            comment=comment
        )
        booking.save()
        booking.locations.set(EventLocation.objects.filter(id__in=locations_pk))
        booking.save()

    return HttpResponse("invalid request")


def add_booking_by_room(request, pk):
    room = Room.objects.get(id=pk)
    events = Event.objects.all()
    data = {
        "title": "Страница бронирования",
        "is_nav_sidebar_enabled": True,
        "available_apps": django.contrib.admin.sites.site.get_app_list(request),
        "room": room,
        "events": events
    }
    return render(request, "main/booking_by_room_page.html", data)


def add_booking_by_event(request, pk):
    event = Event.objects.get(id=pk)
    data = {
        "title": "Страница бронирования",
        "is_nav_sidebar_enabled": True,
        "available_apps": django.contrib.admin.sites.site.get_app_list(request),
        "event": event
    }
    return render(request, "main/booking_by_event_page.html", data)
