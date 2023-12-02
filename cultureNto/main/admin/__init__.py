from django.contrib import admin
from .. import models
from .booking import BookingAdmin
from .event import EventAdmin
from .event_location import EventLocationAdmin
from .event_type import EventTypeAdmin
from .room import RoomAdmin
from .work import WorkAdmin
from .work_type import WorkTypeAdmin


admin.site.register(models.Booking, BookingAdmin)
admin.site.register(models.Event, EventAdmin)
admin.site.register(models.EventLocation, EventLocationAdmin)
admin.site.register(models.EventType, EventTypeAdmin)
admin.site.register(models.Room, RoomAdmin)
admin.site.register(models.Work, WorkAdmin)
admin.site.register(models.WorkType, WorkTypeAdmin)
