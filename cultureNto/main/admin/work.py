from django.contrib.admin import ModelAdmin
from django.utils.html import format_html
from import_export.admin import ImportExportMixin


class WorkAdmin(ImportExportMixin, ModelAdmin):
    list_display = ("date", "time", "colored_status", "work_type", "room", "small_description", "event")

    def small_description(self, obj):
        max_len = 120
        if len(obj.description) > max_len:
            return obj.description[:max_len-3] + "..."
        else:
            return obj.description

    def colored_status(self, obj):
        color = "transparent"
        if obj.status == "Выполнена":
            color = "rgb(201, 199, 199)"
        elif obj.status == "К выполнению":
            color = "pink"
        return format_html(f'<p style="background-color: {color};">{obj.status}</p>')

    colored_status.short_description = "Статус заявки"
    small_description.short_description = "Описание"
