from django.db import models


class ClubType(models.Model):
    name = models.CharField(max_length=255, verbose_name="Вид кружка")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Вид кружка'
        verbose_name_plural = 'Виды кружков'
