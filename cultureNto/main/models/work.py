import datetime
import django
from django.db import models
from django.core.validators import ValidationError
from .event import Event
from .work_type import WorkType
from .room import Room


class Work(models.Model):
    STATUSES = (
        ("Создана(черновик)", "Создана(черновик)"),
        ("К выполнению", "К выполнению"),
        ("Выполнена", "Выполнена")
    )

    date = models.DateField(verbose_name="Дата регистрации заявки")
    time = models.TimeField(verbose_name="Время регистрации заявки")
    event = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name="Мероприятие", null=True, blank=True)
    work_type = models.ForeignKey(WorkType, on_delete=models.CASCADE, verbose_name="Вид работы")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name="Помещение")
    date_end = models.DateField(verbose_name="Конечная дата выполнения заявки", default=datetime.date.today)
    time_end = models.TimeField(verbose_name="Конечное время выполнения заявки", default=django.utils.timezone.now)
    description = models.TextField(verbose_name="Описание", null=True, blank=True)
    status = models.CharField(choices=STATUSES, verbose_name="Статус заявки", max_length=255, default="Создана(черновик)")

    def __str__(self):
        return f"Дата регистрации заявки: {self.date.day}.{self.date.month}.{self.date.year} {self.time.hour}:{self.time.minute}. Вид работы: {self.work_type}. Помещение: {self.room}. Статус: {self.status}"

    def clean(self):
        if datetime.date.today() > self.date_end:
            raise ValidationError \
                ('Дата окончания заявки раньше сегодняшнего дня. Выберите день, который позже, чем сегодня')
        if (self.date > self.date_end) or (self.date == self.date_end and self.time > self.time_end):
            raise ValidationError("Дата регистрации заявки позже, чем конечная дата выполнения заявки.")

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
