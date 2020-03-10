# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from celery import shared_task
from core import applicationIOT
from core.models import Weather
from random import randint


@shared_task
def data_per_half_hour():
    # data = applicationIOT.get_data_device()
    # print(data)
    w = Weather(
        temp_in=randint(40, 60),
        temp_out=randint(40, 60),
        temp_water=randint(40, 60),
        pressure=50,
        humidity_in=50,
        humidity_out=50,
        voltage=34.5
    )
    w.save()
