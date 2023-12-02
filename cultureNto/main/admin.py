from django.contrib import admin
from .models import EventType, Event, Work, WorkType, Room, Booking, EventLocation
from django.utils.html import format_html

admin.site.register(EventType)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("date", "time", "type_event", "small_description", "btn_brone")
    list_filter = ("date", "type_event")

    def small_description(self, obj):
        maxlen = 120
        if len(obj.description) > maxlen:
            return obj.description[:maxlen-3] + "..."
        else:
            return obj.description

    small_description.short_description = "Описание"

    def btn_brone(self, obj):
        return format_html(f'<a href="/add_booking_by_event/{obj.pk}" class="btn_brone">Забронировать помещение</a>')

    btn_brone.short_description = "Забронировать помещение для мероприятия"

    # def get_form(self, request, obj=None, **kwargs):
    #     form = super(EventAdmin, self).get_form(request, obj, **kwargs)
    #     form.base_fields['type_event'].queryset = EventType.objects.filter(pk=1)
    #     print(form)
    #     return form


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ("name", "btn_brone")

    def btn_brone(self, obj):
        return format_html(f'<a href="/add_booking_by_room/{obj.pk}" class="btn_brone">Забронировать данное помещение</a>')

    btn_brone.short_description = "Забронировать"


admin.site.register(WorkType)
admin.site.register(EventLocation)


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ("date", "time", "color_status", "work_type", "room", "small_description", "event")

    def small_description(self, obj):
        maxlen = 120
        if len(obj.description) > maxlen:
            return obj.description[:maxlen-3] + "..."
        else:
            return obj.description

    def color_status(self, obj):
        color = "transparent"
        if obj.status == "Выполнена":
            color = "rgb(201, 199, 199)"
        elif obj.status == "К выполнению":
            color = "pink"
        return format_html(f'<p style="background-color: {color};">{obj.status}</p>')
    color_status.short_description = "Статус заявки"
    small_description.short_description = "Описание"


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    pass
