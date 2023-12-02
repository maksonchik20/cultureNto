import datetime
from django.db import migrations
from django.db.models import Q


def populate_booking(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0006_alter_room_locations"),
    ]

    operations = [
        migrations.RunPython(populate_booking),
    ]
