from django.db import models
from django.core.validators import ValidationError
from django.db.models import Q
from .event import Event
from .event_location import EventLocation


class Booking(models.Model):
    date_create = models.DateField(verbose_name="Дата создания")
    event = models.ForeignKey(Event, verbose_name="Мероприятие", on_delete=models.CASCADE)
    date_start = models.DateTimeField(verbose_name="Дата начала бронирования")
    date_end = models.DateTimeField(verbose_name="Дата окончания бронирования")
    locations = models.ManyToManyField(EventLocation, verbose_name="Помещение")
    comment = models.TextField(verbose_name="Комментарий")

    def __str__(self):
        locations = EventLocation.objects.filter(id__in=self.locations.all())
        locations = ' '.join(location.name[:50] for location in locations)
        return f"Помещения {locations} забронированы с {self.date_start.date()} {self.date_start.time()} до {self.date_end.date()} {self.date_end.time()}. Создано {self.date_create}."

    class Meta:
        verbose_name = "Бронирование"
        verbose_name_plural = "Бронирования"

    @classmethod
    def get_booking_intersection(cls, locations_pk, start_datetime, end_datetime):
        bookings = cls.objects.filter(
            locations__id__in=locations_pk,
        ).exclude(Q(date_end__lt=start_datetime) | Q(date_start__gt=end_datetime))
        return bookings
