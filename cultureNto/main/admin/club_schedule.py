from django.contrib.admin import ModelAdmin
from import_export.admin import ImportExportMixin


class ClubScheduleAdmin(ImportExportMixin, ModelAdmin):
    list_display = ("to_str",)

    def to_str(self, obj):
        return f"{obj.club_registration.all().first().name} ({obj.weekday.name} с {obj.time_start} до {obj.time_end})"

    to_str.short_description = "Кружок"
