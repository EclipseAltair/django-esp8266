# -*- coding: utf-8 -*-
from django.shortcuts import render
from core.models import Weather


def weather(request):
    data = Weather.objects.all().last()
    return render(request, 'core/index.html', locals())
