from django.contrib.admin import ModelAdmin
from django.utils.html import format_html
from import_export.admin import ImportExportMixin


class RoomAdmin(ImportExportMixin, ModelAdmin):
    list_display = ("name", "button_booking")

    def button_booking(self, obj):
        return format_html(
            f'<a href="/add_booking_by_room/{obj.pk}" class="btn_brone">Забронировать данное помещение</a>'
        )

    button_booking.short_description = "Забронировать"
