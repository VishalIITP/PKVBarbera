# webbarbera/urls.py
from os import stat
from webbarbera.settings import MEDIA_ROOT
from django.conf.urls import include
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Barbera Admin Panel"
admin.site.site_title = "Barbera Admin"
admin.site.index_title = "Welcome to Barbera Site Administration"

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('home.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
