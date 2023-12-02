import datetime
from django.db import migrations
from django.db.models import Q


def populate_booking(apps, _schema_editor):
    Booking = apps.get_model("main", "Booking")
    Event = apps.get_model("main", "Event")
    EventLocation = apps.get_model("main", "EventLocation")

    def create_booking(event_id, date_start, date_end, comment, locations_query):
        booking = Booking(
            date_create=datetime.datetime.now(),
            event=Event.objects.get(id=event_id),
            date_start=date_start,
            date_end=date_end,
            comment=comment
        )
        booking.save()
        booking.locations.set(EventLocation.objects.filter(locations_query))

    create_booking(
        event_id=5,
        date_start=datetime.datetime(2023, 11, 22, 9, 45),
        date_end=datetime.datetime(2023, 11, 22, 11, 50),
        comment="Репетиция на театральной сцене",
        locations_query=Q(name="Театральная сцена")
    )

    create_booking(
        event_id=2,
        date_start=datetime.datetime(2023, 11, 25, 11, 50),
        date_end=datetime.datetime(2023, 11, 25, 17, 10),
        comment="Выставка (бронь заранее для размещения)",
        locations_query=Q(name="Арт-галерея (1-й сектор)") | Q(name="Арт-галерея (2-й сектор)")
    )

    create_booking(
        event_id=1,
        date_start=datetime.datetime(2023, 11, 19, 19, 50),
        date_end=datetime.datetime(2023, 11, 19, 22, 30),
        comment="Спектакль",
        locations_query=Q(name="Театральная сцена")
    )


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0006_alter_room_locations"),
    ]

    operations = [
        migrations.RunPython(populate_booking),
    ]
