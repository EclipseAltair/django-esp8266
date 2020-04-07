# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path
from core.views import weather


urlpatterns = [
    # path('data/', data_per_half_hour, name='data'),
    path('', weather, name='weather'),
    path('admin/', admin.site.urls),
]
