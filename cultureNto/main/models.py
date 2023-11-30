import datetime
from django.db import models
# from django.utils import timezone
from django.core.validators import ValidationError
import django
from .utils import Ready

class EventType(models.Model):
    name_event_type = models.CharField(max_length=255, verbose_name="Вид мероприятия")

    def __str__(self):
        return f"{self.name_event_type}"

    class Meta:
        verbose_name = 'Вид мероприятия'
        verbose_name_plural = 'Виды мероприятий'

class Event(models.Model):
    date = models.DateField(verbose_name="Дата мероприятия", default=datetime.date.today)
    time = models.TimeField(verbose_name="Время мероприятия")
    type_event = models.ForeignKey(EventType, on_delete=models.PROTECT, verbose_name="Вид мероприятия")
    description = models.TextField(verbose_name="Описание")
    
    def __str__(self):
        return f"Дата: {self.date.day}.{self.date.month}.{self.date.year} Время: {self.time.hour}:{self.time.minute}. Вид мероприятия: {self.type_event}"

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'

class WorkType(models.Model):
    name = models.CharField(verbose_name="Название вида работы", max_length=255)
    
    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Вид работы'
        verbose_name_plural = 'Виды работ'

class Rooms(models.Model):
    name = models.CharField(verbose_name="Название помещения", max_length=255)
    cnts = models.PositiveIntegerField(verbose_name="Количество частей помещения",
    help_text="""Если этот параметр равен 0, то помещение нельзя забронировать.
    Если же равен 1, то помещение можно забронировать только целиком.
    Если же равен x, то помещение можно разделить(забронировать) на x частей.""",
    default=1
    )
    def __str__(self):
        return f"Название: {self.name}. Количество частей помещения: {self.cnts}"
    
    class Meta:
        verbose_name = 'Помещение'
        verbose_name_plural = 'Помещения'

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
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE, verbose_name="Помещение")
    date_end = models.DateField(verbose_name="Конечная дата выполнения заявки", default=datetime.date.today)
    time_end = models.TimeField(verbose_name="Конечное время выполнения заявки", default=django.utils.timezone.now)
    description = models.TextField(verbose_name="Описание", null=True, blank=True)
    status = models.CharField(choices=STATUSES, verbose_name="Статус заявки", max_length=255, default="Создана(черновик)")

    def __str__(self):
        return f"Дата регистрации заявки: {self.date.day}.{self.date.month}.{self.date.year} {self.time.hour}:{self.time.minute}. Вид работы: {self.work_type}. Помещение: {self.room}. Статус: {self.status}"
    
    def clean(self):
        if datetime.date.today() > self.date_end:
            raise ValidationError('Дата окончания заявки раньше сегодняшнего дня. Выберите день, который позже, чем сегодня')
        if (self.date > self.date_end) or (self.date == self.date_end and self.time > self.time_end):
            raise ValidationError("Дата регистрации заявки позже, чем конечная дата выполнения заявки.")

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

class Booking(models.Model):
    date_create = models.DateField(verbose_name="Дата создания")
    event = models.ForeignKey(Event, verbose_name="Мероприятие", on_delete=models.CASCADE)
    date_start = models.DateTimeField(verbose_name="Дата начала бронирования")
    date_end = models.DateTimeField(verbose_name="Дата окончания бронирования")
    room = models.ForeignKey(Rooms, verbose_name="Помещение", on_delete=models.CASCADE)
    comment = models.TextField(verbose_name="Комментарий")
    cnt_section = models.PositiveIntegerField(verbose_name="Количество забронированных частей", default=1)
    
    def __str__(self):
        return f"Помещение {self.room.name} забранировано с {self.date_start.date()} {self.date_start.time()} до {self.date_end.date()} {self.date_end.time()} на {self.cnt_section} из {self.room.cnts} частей. Создано {self.date_create}."

    def clean(self):
        cnt_free_room = Ready().get_free_room_between_date(self.date_start, self.date_end)
        if (self.cnt_section <= 0):
            raise ValidationError("Убедитесь, что количетсво забронированных частей > 0")
        if (cnt_free_room.get(self.room.pk) is None):
            raise ValidationError("Помещение не было найдено")
        if (self.cnt_section > self.room.cnts):
            raise ValidationError(f"Помещение {self.room.name} нельзя забронировать на {self.cnt_section} части(ей). К бронированию доступно: {cnt_free_room[self.room.pk][1]} частей")
    
    class Meta:
        verbose_name = "Бронирование"
        verbose_name_plural = "Бронирования"
