import django_tables2 as tables
from .models import Event, Room, ClubRegistration
from django.utils.html import format_html
from django_tables2.export.views import ExportMixin

class EventTable(tables.Table):
    class Meta:
        model = Event
        template_name = "django_tables2/bootstrap.html"
        fields = ("date", "type_event", "description", )


class RoomTable(tables.Table):
    class Meta:
        model = Room
        template_name = "django_tables2/bootstrap.html"
        fields = ("name", )


class ClubRegistrationTable(tables.Table):
    class Meta:
        model = ClubRegistration
        template_name = "django_tables2/bootstrap.html"
        fields = ("name", "datetime", "type", "locations", "schedule_type", "schedule", "teacher")

class SimpleTable(ExportMixin, tables.Table):
    name = tables.Column(empty_values=(), verbose_name="Название кружка")
    monday = tables.Column(verbose_name="Понедельник")
    tuesday = tables.Column(verbose_name="Вторник")
    wednesday = tables.Column(verbose_name="Среда")
    thursday = tables.Column(verbose_name="Четверг")
    friday = tables.Column(verbose_name="Пятница")
    saturday = tables.Column(verbose_name="Суббота")
    sunday = tables.Column(verbose_name="Воскресенье")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def render_name(self, value):
        return format_html(f"{value}")
    def render_monday(self, value):
        return format_html(f"{value}")
    def render_tuesday(self, value):
        return format_html(f"{value}")
    def render_wednesday(self, value):
        return format_html(f"{value}")
    def render_thursday(self, value):
        return format_html(f"{value}")
    def render_friday(self, value):
        return format_html(f"{value}")
    def render_saturday(self, value):
        return format_html(f"{value}")
    def render_sunday(self, value):
        return format_html(f"{value}")