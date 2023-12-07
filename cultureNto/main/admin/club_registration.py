from django.contrib.admin import ModelAdmin
from import_export.admin import ImportExportMixin
from ..forms import ClubRegistrationForm
from ..models import ClubRegistration


class ClubRegistrationAdmin(ImportExportMixin, ModelAdmin):
    form = ClubRegistrationForm
    list_display = ("name", "type", "datetime", "teacher")
