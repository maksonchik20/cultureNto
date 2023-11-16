import datetime
from django.db import models


class EventType(models.Model):
    name_event_type = models.CharField(max_length=255, verbose_name="Вид мероприятия")

    def __str__(self):
        return f"{self.name_event_type}"

    class Meta:
        verbose_name = 'Вид мероприятия'
        verbose_name_plural = 'Виды мероприятий'

class Event(models.Model):
    CATEGORY = (
        ("Развлечения", "Развлечения"),
        ("Просвещение", "Просвещение")
    )
    date = models.DateField(verbose_name="Дата мероприятия", default=datetime.date.today)
    time = models.TimeField(verbose_name="Время мероприятия")
    type_event = models.ForeignKey(EventType, on_delete=models.PROTECT, verbose_name="Вид мероприятия")
    description = models.TextField(verbose_name="Описание")
    category = models.CharField(choices=CATEGORY, verbose_name="Категория", max_length=255, default="Развлечения")

    def __str__(self):
        return f"Категория: {self.category}. Дата: {self.date.day}.{self.date.month}.{self.date.year} Время: {self.time.hour}:{self.time.minute}. Вид мероприятия: {self.type_event}"

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'