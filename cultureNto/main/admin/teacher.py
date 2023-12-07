from django.contrib.admin import ModelAdmin
from import_export.admin import ImportExportMixin
from ..models import Teacher


class TeacherAdmin(ImportExportMixin, ModelAdmin):
    list_display = ("__str__", "last_name", "first_name", "middle_name")
