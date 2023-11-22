from django.contrib import admin
from .models import EventType, Event, Work, WorkType, Rooms
from django.utils.html import format_html

admin.site.register(EventType)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("date", "time", "type_event", "small_description")
    list_filter = ("date", "type_event")
    def small_description(self, obj):
        maxlen = 120
        if (len(obj.description) > maxlen):
            return (obj.description)[:maxlen-3] + "..."
        else:
            return obj.description
    small_description.short_description  = "Описание"

admin.site.register(Rooms)
admin.site.register(WorkType)

@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ("date", "time", "color_status", "work_type", "room", "small_description", "event")
    # list_filter = ("date", "type_event")
    def small_description(self, obj):
        maxlen = 120
        if (len(obj.description) > maxlen):
            return (obj.description)[:maxlen-3] + "..."
        else:
            return obj.description
    def color_status(self, obj):
        color = "transparent"
        if (obj.status == "Выполнена"):
            color = "rgb(201, 199, 199)"
        elif (obj.status == "К выполнению"):
            color = "pink"
        return format_html(f'<p style="background-color: {color};">{obj.status}</p>')
    color_status.short_description = "Статус заявки"
    small_description.short_description  = "Описание"
