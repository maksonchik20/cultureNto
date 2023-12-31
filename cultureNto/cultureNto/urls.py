from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.index_title = "Администрирование Культуры"
admin.site.site_title = "Администрирование Культуры"
admin.site.site_header = "Администрирование Культуры"

urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
