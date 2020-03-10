# -*- coding: utf-8 -*-
from django.shortcuts import render
from core.models import Weather
from core import applicationIOT


def weather(request):
    data = Weather.objects.all().last()
    charts = Weather.objects.all().order_by('-id')[:48]
    return render(request, 'core/index.html', locals())
