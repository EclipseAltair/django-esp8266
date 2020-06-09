# -*- coding: utf-8 -*-
from django.urls import path
from .views import main, graphs


urlpatterns = [
    path('', main, name='main'),
    path('graphs', graphs, name='graphs'),
]
