# -*- coding: utf-8 -*-
from django.shortcuts import render
from core.models import Weather


def main(request):
    data = Weather.objects.all().last()
    return render(request, 'core/index.html', locals())


def graphs(request):
    charts = Weather.objects.all().order_by('-id')[:256]
    return render(request, 'core/graphs.html', locals())
