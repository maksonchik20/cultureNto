from import_export.resources import ModelResource
from ..models import Room


class RoomResource(ModelResource):
    class Meta:
        model = Room
