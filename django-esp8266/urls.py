# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('core.urls')),
    path('', include('device.urls')),
    path('admin/', admin.site.urls),
]
