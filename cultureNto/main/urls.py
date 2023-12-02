from django.urls import path, include, re_path
from django.contrib import admin
from .views import *


admin.site.site_header = "Администрирование Культуры"
admin.site.site_title = "Администрирование Культуры"
admin.site.index_title = "Добро пожаловать"


urlpatterns = [
    path('', index),
    path("entertainment/", entertainment),
    path("enlightenment/", enlightenment),
    path("education/", education),
    path("worktable/", worktable),
    path("rooms/", rooms),

    path("add_booking_by_room/<int:pk>", add_booking_by_room),
    path("add_booking_by_event/<int:pk>", add_booking_by_event),
    path("get_booking_intersection", get_booking_intersection),
    path("get_available_rooms", get_available_rooms),
    path("add_booking", add_booking),
    
    # path("tabletest/", tableRender)
]
