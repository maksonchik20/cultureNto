from import_export.resources import ModelResource
from ..models import WorkType


class WorkTypeResource(ModelResource):
    class Meta:
        model = WorkType
