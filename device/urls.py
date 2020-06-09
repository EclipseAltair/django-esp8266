# -*- coding: utf-8 -*-
from django.urls import path
from .views import device


urlpatterns = [
    path('device', device, name='main'),
]
