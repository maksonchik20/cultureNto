from import_export.resources import ModelResource
from ..models import Booking


class BookingResource(ModelResource):
    class Meta:
        model = Booking
