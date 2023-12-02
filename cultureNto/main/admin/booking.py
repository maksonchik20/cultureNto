from django.contrib.admin import ModelAdmin
from import_export.admin import ImportExportMixin
from ..forms import BookingForm


class BookingAdmin(ImportExportMixin, ModelAdmin):
    form = BookingForm
