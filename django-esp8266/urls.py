# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path
from core.views import weather

urlpatterns = [
    # path('api/', api, name='api'),
    path('', weather, name='weather'),
    path('admin/', admin.site.urls),
]
