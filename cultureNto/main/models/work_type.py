from django.db import models


class WorkType(models.Model):
    name = models.CharField(verbose_name="Название вида работы", max_length=255)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Вид работы'
        verbose_name_plural = 'Виды работ'
