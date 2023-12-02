from django.contrib.admin import ModelAdmin
from django.utils.html import format_html
from import_export.admin import ImportExportMixin


class EventAdmin(ImportExportMixin, ModelAdmin):
    list_display = ("date", "time", "type_event", "small_description", "button_booking")
    list_filter = ("date", "type_event")

    def small_description(self, obj):
        max_len = 120
        if len(obj.description) > max_len:
            return obj.description[:max_len-3] + "..."
        else:
            return obj.description

    small_description.short_description = "Описание"

    def button_booking(self, obj):
        return format_html(f'<a href="/add_booking_by_event/{obj.pk}" class="btn_brone">Забронировать помещение</a>')

    button_booking.short_description = "Забронировать помещение для мероприятия"
