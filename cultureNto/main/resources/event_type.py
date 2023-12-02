from import_export.resources import ModelResource
from ..models import EventType


class EventTypeResource(ModelResource):
    class Meta:
        model = EventType
