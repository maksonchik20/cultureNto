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
    path("admin/brone", page_brone)
    
    # path("tabletest/", tableRender)
]
