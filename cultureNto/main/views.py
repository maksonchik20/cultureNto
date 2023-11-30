from datetime import datetime
from django.shortcuts import render, redirect
from django_tables2 import SingleTableView, RequestConfig
from django_tables2.export.views import ExportMixin
from .models import Event, EventType, Work, WorkType, Rooms
from .tables import EventTable, RoomTable
from django_tables2.export.export import TableExport

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

def createData(request):
    # eventTypes = ["Спектакль", "Концерт", "Репетиция", "Выставка", "Секции"]
    # for et in eventTypes:
    #     EventType.objects.create(name_event_type=et)
#     event = [("19.11.2023", "8.00 PM", "Спектакль", """"Волшебная Ночь Звезд: Театральное Путешествие"

# Добро пожаловать на удивительное театральное событие, которое разгадывает тайны ночного неба! Спектакль "Волшебная Ночь Звезд" приглашает вас в захватывающее путешествие по звездному космосу, где каждая звезда рассказывает свою уникальную историю.

# Это увлекательное шоу сочетает в себе элементы фэнтези, мистики и волшебства, создавая атмосферу загадочности и великолепия. Артисты, великолепные костюмы и магическая музыкальная аранжировка переносят зрителей в мир, где каждая звезда является символом сновидений, желаний и вдохновения.

# Спектакль будет проходить в театре "Звездная Сцена" в этот особенный вечер 19 числа. Приготовьтесь к тому, чтобы пережить невероятные моменты, которые расскажут вам о волшебстве ночного неба и пробудят в вас детскую веру в чудеса. "Волшебная Ночь Звезд" - это не просто представление, это приключение, которое оставит незабываемые впечатления и вдохновит вас на свершения."""),
#             ("25.12.2023", "1.30 PM", "Выставка", "Просвещение", """"Гармония Творчества: Искусство в Каждом Жесте"

# Откройте двери в мир бескрайнего творчества на нашей захватывающей выставке "Гармония Творчества". Это уникальное мероприятие представит вам широкий спектр художественных произведений, созданных талантливыми художниками, скульпторами и фотографами.

# На этой выставке каждая картина, скульптура или фотография - это не просто произведение искусства, а настоящая история, рассказанная визуальным языком. Вы сможете окунуться в мир красок, форм и эмоций, испытывая гармонию и восторг от каждого произведения.

# "Гармония Творчества" приглашает вас на увлекательное путешествие по искусству, где каждое произведение станет мостом между разными культурами, стилями и выражениями. Приходите на выставку в наш галерейный пространство 25 числа, чтобы поддаться волшебству творчества и насладиться красотой многообразия художественных форм. Это событие станет вдохновляющим праздником искусства для всех любителей красоты и творчества."""),
# ("22.01.2024", "10.00 AM", "Репетиция", """"Магия Творческого Слияния: Репетиция Симфонии 25.01.2024"

# 22 января 2024 года приглашаем вас стать свидетелями захватывающего момента творчества на репетиции уникальной симфонии "Магия Творческого Слияния". Этот вечер будет посвящен звуковому слиянию инструментов и голосов, создающих мощный вихрь эмоций и вдохновения.

# Великие музыканты сойдутся в этот вечер, чтобы согреть вас звуковыми волнениями и представить уникальное исполнение симфонии, которая звучит как путешествие сквозь пространство и время. Это репетиция, где каждая нота, каждый аккорд — шаг к созданию волшебства, которое охватит вас во время грандиозного выступления.

# Присоединитесь к нам в зале репетиций 22 января 2024 года и погрузитесь в атмосферу творческой лаборатории, где искусство и страсть соединяются в единое целое. Это будет неповторимая возможность заглянуть в застенки создания великой симфонии и почувствовать энергию творческого процесса.""")
# ]
#     for ev in event:
#         Event.objects.create(date=datetime.strptime(ev[0], "%d.%m.%Y"),
#                             time=datetime.strptime(ev[1], "%I.%M %p"),
#                             type_event = EventType.objects.get(name_event_type=ev[2]),
#                             description = ev[3],
#                             )
    # rooms = ["Арт-галерея", "Выставочный зал", "Театральная сцена", "Конференц-зал", "Мастерская", "Танцевальный зал", "Гардероб", "Кафе", "Библиотека", "Лекторий", "Комната отдыха для артистов", "Комната звукооператора и светотехника"]
    # for room in rooms:
    #     Rooms.objects.create(name=room)
    # work_types = ["Костюмер",
    #             "Секретарь",
    #             "Бухгалтер",
    #             "Координатор по обслуживанию гостей",
    #             "Менеджер по маркетингу и продвижению",
    #             "Гардеробщик",
    #             "Координатор",
    #             "Светотехник(Работа с осветительным оборудованием)",
    #             "Звукорежиссер(Настройка и управление звуковым оборудованием)",
    #             "Разработка концепции мероприятий(декораций, освещения и атмосферы)",
    #             "Организация культурных событий",
    #             "Лектор(Проведение лекций/мастер-классов)"]
    # for work_type in work_types:
    #     WorkType.objects.create(name=work_type)
    return render(request, "main/index.html")

# class EventRazvlechListView(ExportMixin, SingleTableView):
#     model = Event
#     table_class = EventTabel
#     table_data = Event.objects.filter(category="Развлечения")
#     template_name = 'main/table.html'

def tableRender(request):
    sl = {
        "prosvesh": "Просвещение",
        "razvlech": "Развлечения",
        "education": "Образование"
    }
    if ("prosvesh" in request.path):
        cat = sl["prosvesh"]
    elif ("razvlech" in request.path):
        cat = sl["razvlech"]
    else:
        cat = sl["education"]
    data = {"title": f"Страница {cat}",
            "header_text": f"Страница {cat}",
            "cat": cat
        }
    if ("prosvesh" in request.path or "razvlech" in request.path):
        table = EventTable(Event.objects.all())
        RequestConfig(request, paginate={"per_page": 2}).configure(table)
        export_format = request.GET.get("_export", None)
        if TableExport.is_valid_format(export_format):
            exporter = TableExport(export_format, table)
            return exporter.response(f"table.{export_format}")
        data["table"] = table
    tableRoom = RoomTable(Rooms.objects.all())
    RequestConfig(request, paginate={"per_page": 8}).configure(tableRoom)
    data["rooms"] = tableRoom
    return render(request, "main/category_page.html", data)

def roomsRender(request):
    data = {"title": f"Страница Помещений",
            "header_text": f"Страница Помещений",
        }
    table = RoomTable(Rooms.objects.all())
    RequestConfig(request, paginate={"per_page": 8}).configure(table)
    export_format = request.GET.get("_export", None)
    if TableExport.is_valid_format(export_format):
        exporter = TableExport(export_format, table)
        return exporter.response(f"table.{export_format}")
    data["table"] = table
    return render(request, "main/rooms.html", data)

def worktable(request):
    if (request.GET.get("del", None) is not None and Work.objects.filter(pk=request.GET.get("del", None)).exists()):
        work_obj = Work.objects.get(pk=request.GET.get("del", None))
        work_obj.status = "Выполнена"
        work_obj.save()
    work_type = request.GET.get('select', "all")
    obj = []
    if (work_type == "all"):
        obj = Work.objects.filter(status="К выполнению")
    else:
        if (WorkType.objects.filter(name=work_type).exists()):
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
