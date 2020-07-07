# -*- coding: utf-8 -*-
from django.shortcuts import render
from core.models import Weather
from . import applicationIOT

MONTH = {
    '01': 'Января',
    '02': 'Февраля',
    '03': 'Марта',
    '04': 'Апреля',
    '05': 'Мая',
    '06': 'Июня',
    '07': 'Июля',
    '08': 'Августа',
    '09': 'Сентября',
    '10': 'Октября',
    '11': 'Ноября',
    '12': 'Декабря',
}


def main(request):
    data_weather = Weather.objects.all().last()
    date = str(data_weather.time)
    month = MONTH[date[5:7]]
    day = date[8:10]
    hours = (int(date[11:13])+3)%24
    minutes = date[14:16]
    return render(request, 'core/index.html', locals())


def graphs(request):
    charts = Weather.objects.all().order_by('-id')[:336]

    dates  = []
    for chart in charts:
        date = str(chart.time)
        month = MONTH[date[5:7]]
        day = date[8:10]
        hours = (int(date[11:13]) + 3) % 24
        minutes = date[14:16]

        dates.append('{} {} {}:{}'.format(day, month, hours, minutes))


    return render(request, 'core/graphs.html', locals())

