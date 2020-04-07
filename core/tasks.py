# # -*- coding: utf-8 -*-
# from __future__ import absolute_import, unicode_literals
#
# from celery import shared_task
# from core import applicationIOT
# from core.models import Weather
#
#
# @shared_task
# def data_per_half_hour():
#     data = applicationIOT.get_data_device()
#     w = Weather(
#         temp_in=data['ti'],
#         temp_out=data['to'],
#         temp_water=data['tw'],
#         pressure=data['pr'],
#         humidity_in=data['hi'],
#         humidity_out=data['ho'],
#         voltage=data['vt']
#     )
#     w.save()
