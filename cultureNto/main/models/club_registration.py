import datetime
from django.db import models
from .club_type import ClubType
from .event_location import EventLocation
from .club_schedule import ClubSchedule
from .teacher import Teacher


class ClubRegistration(models.Model):
    class ScheduleTypeEnum(models.IntegerChoices):
        TIMES_1 = 1, '1 раз в неделю'
        TIMES_2 = 2, '2 раза в неделю'
        TIMES_3 = 3, '3 раза в неделю'

    name = models.CharField(max_length=255, verbose_name="Название кружка")
    datetime = models.DateTimeField(verbose_name="Дата начала работы кружка")
    type = models.ForeignKey(ClubType, on_delete=models.CASCADE, verbose_name="Вид кружка")
    locations = models.ManyToManyField(EventLocation, verbose_name="Помещение", related_name="club_registration")
    schedule_type = models.IntegerField(choices=ScheduleTypeEnum.choices, verbose_name="Вариант расписания")
    schedule = models.ManyToManyField(ClubSchedule, verbose_name="Расписание", related_name="club_registration")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name="Преподаватель")

    def delete(self, using=None, keep_parents=False):
        ClubSchedule.objects.filter(id__in=self.schedule.all()).delete()
        super().delete(using=using, keep_parents=keep_parents)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Регистрация кружка'
        verbose_name_plural = 'Регистрации кружков'

    @classmethod
    def get_club_schedule_intersection(cls, locations_pk, start_datetime, end_datetime):
        start_datetime = datetime.datetime(1, 1, start_datetime.weekday() + 1, start_datetime.hour, start_datetime.minute, start_datetime.second)
        end_datetime = datetime.datetime(1, 1, end_datetime.weekday() + 1, end_datetime.hour, end_datetime.minute, end_datetime.second)

        club_registration = ClubRegistration.objects.filter(
            locations__in=locations_pk
        ).distinct()

        result = []

        for cr in club_registration:
            exclude = True

            for s in cr.schedule.all():
                if datetime.datetime(1, 1, s.weekday.id, s.time_end.hour, s.time_end.minute, s.time_end.second) < start_datetime:
                    continue

                if datetime.datetime(1, 1, s.weekday.id, s.time_end.hour, s.time_end.minute, s.time_end.second) > end_datetime:
                    continue

                exclude = False
                break

            if not exclude:
                result.append(cr)

        return result
