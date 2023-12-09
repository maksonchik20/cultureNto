from django.contrib.admin import ModelAdmin
from import_export.admin import ImportExportMixin
from ..forms import ClubRegistrationForm
from ..models import Weekday, ClubRegistration


class ClubRegistrationAdmin(ImportExportMixin, ModelAdmin):
    change_form_template = "main/club_registration_form.html"
    form = ClubRegistrationForm
    list_display = ("name", "type", "datetime", "teacher")

    fields = (
        "name",
        "teacher",
        "datetime",
        "type",
        "locations",
        "schedule_type",
        ("schedule_day_1", "schedule_time_start_1", "schedule_time_end_1"),
        ("schedule_day_2", "schedule_time_start_2", "schedule_time_end_2"),
        ("schedule_day_3", "schedule_time_start_3", "schedule_time_end_3")
    )

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['weekdays'] = Weekday.objects.all()
        extra_context['related_schedule'] = ClubRegistration.objects.get(pk=object_id).schedule.all()
        return super(ClubRegistrationAdmin, self).change_view(request, object_id, form_url, extra_context)

    class Media:
        js = ['main/admin.js']
