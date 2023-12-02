import django_tables2 as tables
from .models import Event, Room


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
