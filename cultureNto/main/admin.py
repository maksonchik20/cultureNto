from django.contrib import admin
from .models import EventType, Event
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

