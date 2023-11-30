from django.db import models
from django.core.validators import ValidationError
from .event import Event
from .room import Room
from .event_location import EventLocation
from .utils import Ready


class Booking(models.Model):
    date_create = models.DateField(verbose_name="Дата создания")
    event = models.ForeignKey(Event, verbose_name="Мероприятие", on_delete=models.CASCADE)
    date_start = models.DateTimeField(verbose_name="Дата начала бронирования")
    date_end = models.DateTimeField(verbose_name="Дата окончания бронирования")
    locations = models.ManyToManyField(EventLocation, verbose_name="Помещение")
    comment = models.TextField(verbose_name="Комментарий")

    def __str__(self):
        return f"Помещение {self.room.name} забранировано с {self.date_start.date()} {self.date_start.time()} до {self.date_end.date()} {self.date_end.time()}. Создано {self.date_create}."

    def clean(self):
        cnt_free_room = Ready().get_free_room_between_date(self.date_start, self.date_end)
        #if (self.cnt_section <= 0):
        #    raise ValidationError("Убедитесь, что количетсво забронированных частей > 0")
        #if (cnt_free_room.get(self.room.pk) is None):
        #    raise ValidationError("Помещение не было найдено")
        #if (self.cnt_section > self.room.cnts):
        #    raise ValidationError(
        #        f"Помещение {self.room.name} нельзя забронировать на {self.cnt_section} части(ей). К бронированию доступно: {cnt_free_room[self.room.pk][1]} частей")

    class Meta:
        verbose_name = "Бронирование"
        verbose_name_plural = "Бронирования"
