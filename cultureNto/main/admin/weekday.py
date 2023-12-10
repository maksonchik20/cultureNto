from django.contrib.admin import ModelAdmin
from import_export.admin import ImportExportMixin


class WeekdayAdmin(ImportExportMixin, ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return False