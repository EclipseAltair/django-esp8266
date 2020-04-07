# -*- coding: utf-8 -*-
from django.shortcuts import render
from core import applicationIOT
from core.models import Weather


def weather(request):
    data = applicationIOT.get_data_device()
    print('DATA', data)
    w = Weather(
        temp_in=data['ti'],
        temp_out=data['to'],
        temp_water=data['tw'],
        pressure=data['pr'],
        humidity_in=data['hi'],
        humidity_out=data['ho'],
        voltage=data['vo'],
        rain=data['ra']
    )
    w.save()
    data = Weather.objects.all().last()
    charts = Weather.objects.all().order_by('-id')[:48]
    return render(request, 'core/index.html', locals())
