from django.db import models


class Weekday(models.Model):
    name = models.CharField(max_length=60, verbose_name="Название")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'День недели'
        verbose_name_plural = 'Дни недели'
