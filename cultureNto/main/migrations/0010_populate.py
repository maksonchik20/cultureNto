import datetime
from django.db import migrations
from django.db.models import Q


def populate_weekday(apps, schema_editor):
    Weekday = apps.get_model("main", "Weekday")

    Weekday.objects.using(schema_editor.connection.alias).bulk_create(
        [
            Weekday(name="Понедельник"),
            Weekday(name="Вторник"),
            Weekday(name="Среда"),
            Weekday(name="Четверг"),
            Weekday(name="Пятница"),
            Weekday(name="Суббота"),
            Weekday(name="Воскресенье"),
        ]
    )


def populate_teacher(apps, schema_editor):
    Teacher = apps.get_model("main", "Teacher")

    Teacher.objects.using(schema_editor.connection.alias).bulk_create(
        [
            Teacher(
                first_name="Иван",
                middle_name="Брониславович",
                last_name="Петров"
            ),
            Teacher(
                first_name="Любовь",
                middle_name="Алексеевна",
                last_name="Дмитриевна"
            ),
            Teacher(
                first_name="Татьяна",
                middle_name="Михайловна",
                last_name="Иванова"
            ),
            Teacher(
                first_name="Лариса",
                middle_name="Николаевна",
                last_name="Филлипова"
            )
        ]
    )


def populate_club_type(apps, schema_editor):
    ClubType = apps.get_model("main", "ClubType")

    ClubType.objects.using(schema_editor.connection.alias).bulk_create(
        [
            ClubType(name="Естественнонаучное направление"),
            ClubType(name="Социально-педагогическое направление"),
            ClubType(name="Техническое направление"),
            ClubType(name="Туристко-краеведческое направление"),
            ClubType(name="Физкультурно-спортивное направление"),
            ClubType(name="Художественное направление")
        ]
    )


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0009_clubscheduletype_clubtype_teacher_weekday_and_more"),
    ]

    operations = [
        migrations.RunPython(populate_weekday),
        migrations.RunPython(populate_teacher),
        migrations.RunPython(populate_club_type),
    ]
