import datetime
import os

from django.db import migrations


def populate_event_location(apps, schema_editor):
    EventLocation = apps.get_model("main", "EventLocation")

    EventLocation.objects.using(schema_editor.connection.alias).bulk_create(
        [
            EventLocation(name="Арт-галерея (1-й сектор)"),
            EventLocation(name="Арт-галерея (2-й сектор)"),
            EventLocation(name="Выставочный зал (1-й сектор)"),
            EventLocation(name="Выставочный зал (2-й сектор)"),
            EventLocation(name="Школьная сцена"),
            EventLocation(name="Конференц-зал"),
            EventLocation(name="Мастерская"),
            EventLocation(name="Танцевальный зал (1-й сектор)"),
            EventLocation(name="Танцевальный зал (2-й сектор)"),
            EventLocation(name="Гардероб"),
            EventLocation(name="Кафе"),
            EventLocation(name="Библиотека"),
            EventLocation(name="Лекторий"),
            EventLocation(name="Комната отдыха для артистов"),
            EventLocation(name="Комната звукооператора и светотехника")
        ]
    )


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0003_eventlocation_remove_booking_cnt_section_and_more"),
    ]

    operations = [
        migrations.RunPython(populate_event_location),
    ]
