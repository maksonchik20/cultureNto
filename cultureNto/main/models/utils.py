# from .models import Rooms, Booking - cyclic import
from django.db.models import Q
from django.apps import apps

class Ready:
    def __init__(self):
        self.Booking = apps.get_model(app_label="main", model_name='Booking')
        self.Rooms = apps.get_model(app_label="main", model_name="Rooms")
    
    # Пример: get_booking_between_date("2023-11-29 09:00:00", "2023-11-29 16:00:00")
    # дату принимает в любом формате
    # Возвращает все брони которые пересекаются с [date_start, date_end]
    def get_booking_between_date(self, date_start, date_end):
        bookings = self.Booking.objects.exclude(Q(date_end__lt=date_start) | Q(date_start__gt=date_end))
        return bookings

    # Для 2 задания
    # возвращает словарь key - roomPk, value - пара [nameRoom, количество свободных частей]
    def get_free_room_between_date(self, date_start, date_end):
        all_rooms = {}
        #for el in self.Rooms.objects.filter(cnts__gte=1):
        #    all_rooms[el.pk] = [el.name, el.cnts]
        ##for el in self.get_booking_between_date(date_start, date_end):
        #    if (all_rooms.get(el.room.pk) is not None):
        #        all_rooms[el.room.pk][1] -= el.cnt_section
        return all_rooms
        