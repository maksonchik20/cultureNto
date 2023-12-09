import datetime
from django.db import migrations
from django.db.models import Q
from ..models import ClubRegistration as _ClubRegistraion


def populate_club_schedule(apps, schema_editor):
    ClubSchedule = apps.get_model("main", "ClubSchedule")
    Weekday = apps.get_model("main", "Weekday")

    ClubSchedule.objects.using(schema_editor.connection.alias).bulk_create([
        ClubSchedule(
            id=1,
            weekday=Weekday.objects.get(id=2),
            time_start=datetime.time(17, 50),
            time_end=datetime.time(19, 20),
        ),
        ClubSchedule(
            id=2,
            weekday=Weekday.objects.get(id=4),
            time_start=datetime.time(17, 50),
            time_end=datetime.time(19, 20),
        ),
        ClubSchedule(
            id=3,
            weekday=Weekday.objects.get(id=3),
            time_start=datetime.time(11, 50),
            time_end=datetime.time(13, 30),
        ),
        ClubSchedule(
            id=4,
            weekday=Weekday.objects.get(id=1),
            time_start=datetime.time(15, 50),
            time_end=datetime.time(16, 30),
        ),
        ClubSchedule(
            id=5,
            weekday=Weekday.objects.get(id=2),
            time_start=datetime.time(17, 50),
            time_end=datetime.time(18, 30),
        ),
        ClubSchedule(
            id=6,
            weekday=Weekday.objects.get(id=3),
            time_start=datetime.time(19, 50),
            time_end=datetime.time(20, 30),
        ),
        ClubSchedule(
            id=7,
            weekday=Weekday.objects.get(id=1),
            time_start=datetime.time(16, 0),
            time_end=datetime.time(17, 0),
        ),
        ClubSchedule(
            id=8,
            weekday=Weekday.objects.get(id=4),
            time_start=datetime.time(16, 0),
            time_end=datetime.time(18, 0),
        ),
        ClubSchedule(
            id=9,
            weekday=Weekday.objects.get(id=5),
            time_start=datetime.time(17, 0),
            time_end=datetime.time(18, 0),
        ),
    ])


def populate_club_registration(apps, schema_editor):
    ClubRegistration = apps.get_model("main", "ClubRegistration")
    ClubSchedule = apps.get_model("main", "ClubSchedule")
    EventLocation = apps.get_model("main", "EventLocation")
    ClubType = apps.get_model("main", "ClubType")
    Teacher = apps.get_model("main", "Teacher")

    def club_registration(name, datetime, type, locations_query, schedule_type, schedule_query, teacher):
        cr = ClubRegistration(
            name=name,
            datetime=datetime,
            type=type,
            schedule_type=schedule_type,
            teacher=teacher
        )
        cr.save()
        cr.locations.set(EventLocation.objects.filter(locations_query))
        cr.schedule.set(ClubSchedule.objects.filter(schedule_query))

    club_registration(
        name="Обучение актёрскому мастерству",
        datetime=datetime.datetime(2023, 11, 19),
        type=ClubType.objects.get(name="Творческое направление"),
        locations_query=Q(name="Школьная сцена"),
        schedule_type=_ClubRegistraion.ScheduleTypeEnum.TIMES_2,
        schedule_query=Q(id=1) | Q(id=2),
        teacher=Teacher.objects.get(first_name="Лариса")
    )

    club_registration(
        name="Обучение программированию",
        datetime=datetime.datetime(2023, 12, 5),
        type=ClubType.objects.get(name="Техническое направление"),
        locations_query=Q(name="Лекторий"),
        schedule_type=_ClubRegistraion.ScheduleTypeEnum.TIMES_1,
        schedule_query=Q(id=3),
        teacher=Teacher.objects.get(first_name="Татьяна")
    )

    club_registration(
        name="Уроки танцев",
        datetime=datetime.datetime(2023, 6, 9),
        type=ClubType.objects.get(name="Хореография"),
        locations_query=Q(name="Танцевальный зал (1-й сектор)") | Q(name="Танцевальный зал (2-й сектор)"),
        schedule_type=_ClubRegistraion.ScheduleTypeEnum.TIMES_3,
        schedule_query=Q(id=4) | Q(id=5) | Q(id=6),
        teacher=Teacher.objects.get(first_name="Любовь")
    )

    club_registration(
        name="Гончарная студия",
        datetime=datetime.datetime(2023, 7, 3),
        type=ClubType.objects.get(name="Техническое направление"),
        locations_query=Q(name="Мастерская"),
        schedule_type=_ClubRegistraion.ScheduleTypeEnum.TIMES_3,
        schedule_query=Q(id=7) | Q(id=8) | Q(id=9),
        teacher=Teacher.objects.get(first_name="Иван")
    )


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0013_alter_booking_comment"),
    ]

    operations = [
        migrations.RunPython(populate_club_schedule),
        migrations.RunPython(populate_club_registration),
    ]
