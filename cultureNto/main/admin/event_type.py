from django.contrib.admin import ModelAdmin
from import_export.admin import ImportExportMixin


class EventTypeAdmin(ImportExportMixin, ModelAdmin):
    pass
