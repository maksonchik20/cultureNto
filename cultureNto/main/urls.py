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
<<<<<<< HEAD
    path("events/", events)
=======
    path("admin/brone", page_brone)
>>>>>>> 4e2f7ef7db715ab957dbad3de51425564d269c00
    
    # path("tabletest/", tableRender)
]
