from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('base/', base),
    path('', index),
    path("razvlech/", tableRender, name="razvlech"),
    path("prosvesh/", tableRender),
    path("education/", tableRender),
    path("createData/", createData),
    path("worktable/", worktable),
    path("start_workers_page/", start_workers_page),
    path("rooms/", roomsRender),
    path("events/", events),

    path("admin/brone", page_brone),
    path("add_booking_by_room/<int:pk>", add_booking_by_room),
    path("add_booking_by_event/<int:pk>", add_booking_by_event),
    path("get_booking_intersection", get_booking_intersection),
    path("get_available_rooms", get_available_rooms),
    path("add_booking", add_booking),
    
    # path("tabletest/", tableRender)
]
