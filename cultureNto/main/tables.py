import django_tables2 as tables
from .models import Event

class EventTabel(tables.Table):
    class Meta:
        model = Event
        template_name = "django_tables2/bootstrap.html"
        fields = ("date", "type_event", "description", )
