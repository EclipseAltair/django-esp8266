# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path
from core.views import graphs, main


urlpatterns = [
    path('', main, name='main'),
    path('graphs', graphs, name='graphs'),
    path('admin/', admin.site.urls),
]
