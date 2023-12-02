from import_export.resources import ModelResource
from ..models import Work


class WorkResource(ModelResource):
    class Meta:
        model = Work
