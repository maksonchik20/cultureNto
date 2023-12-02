from import_export.resources import ModelResource
from ..models import EventLocation


class EventLocationResource(ModelResource):
    class Meta:
        model = EventLocation
