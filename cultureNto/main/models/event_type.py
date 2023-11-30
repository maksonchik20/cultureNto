from django.db import models


class EventType(models.Model):
    name_event_type = models.CharField(max_length=255, verbose_name="Вид мероприятия")

    def __str__(self):
        return f"{self.name_event_type}"

    class Meta:
        verbose_name = 'Вид мероприятия'
        verbose_name_plural = 'Виды мероприятий'
