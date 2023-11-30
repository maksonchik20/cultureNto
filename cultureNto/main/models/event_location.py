from django.db import models


class EventLocation(models.Model):
    name = models.CharField(verbose_name="Название", max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Место проведения мероприятия'
        verbose_name_plural = 'Места проведения мероприятий'
