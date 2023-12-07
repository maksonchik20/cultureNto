from django.db import models
from .weekday import Weekday


class ClubSchedule(models.Model):
    weekday = models.ForeignKey(Weekday, on_delete=models.CASCADE, verbose_name="День недели")
    time_start = models.TimeField(verbose_name="Время начала занятий")
    time_end = models.TimeField(verbose_name="Время окончания занятий")

    def __str__(self):
        return f"{self.weekday} ({self.time_start} - {self.time_end})"

    class Meta:
        verbose_name = 'Расписание кружка'
        verbose_name_plural = 'Расписание кружков'
