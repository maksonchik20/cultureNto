from django.forms import ModelForm, ValidationError
from ..models import Booking


class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

    def clean(self):
        locations = self.cleaned_data.get('locations')
        date_start = self.cleaned_data.get('date_start')
        date_end = self.cleaned_data.get('date_end')
        intersection = Booking.get_booking_intersection(locations, date_start, date_end)
        if len(intersection) != 0:
            raise ValidationError("Данная бронь пересекается с другими мероприятиями.")

        return self.cleaned_data
