from django.contrib.admin import ModelAdmin
from import_export.admin import ImportExportMixin


class ClubScheduleAdmin(ImportExportMixin, ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
        
    list_display = ("to_str",)

    def to_str(self, obj):
        return f"{obj.club_registration.all().first().name} ({obj.weekday.name} с {obj.time_start} до {obj.time_end})"

    to_str.short_description = "Кружок"
