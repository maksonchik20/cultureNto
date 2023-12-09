from django.contrib.admin import ModelAdmin
from import_export.admin import ImportExportMixin


class ClubTypeAdmin(ImportExportMixin, ModelAdmin):
    pass
