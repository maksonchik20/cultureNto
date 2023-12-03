import datetime
from django.db import models
from .event_type import EventType


class Event(models.Model):
    date = models.DateField(verbose_name="Дата", default=datetime.date.today)
    time = models.TimeField(verbose_name="Время")
    type_event = models.ForeignKey(EventType, on_delete=models.PROTECT, verbose_name="Вид")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return f"Дата: {self.date.day}.{self.date.month}.{self.date.year} Время: {self.time.hour}:{self.time.minute}.\n{self.description[:50]}"

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'
