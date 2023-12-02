from import_export.resources import ModelResource
from ..models import Event


class EventResource(ModelResource):
    class Meta:
        model = Event
