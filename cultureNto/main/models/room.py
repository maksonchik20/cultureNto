from django.db import models
from .event_location import EventLocation


class Room(models.Model):
    name = models.CharField(verbose_name="Название помещения", max_length=255)
    locations = models.ManyToManyField(EventLocation, verbose_name="Части помещения", related_name="room")

    def __str__(self):
        return f"Название: {self.name}"

    class Meta:
        verbose_name = 'Помещение'
        verbose_name_plural = 'Помещения'
