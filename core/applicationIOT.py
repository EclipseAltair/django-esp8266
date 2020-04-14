# -*- coding: utf-8 -*-
import wiotp.sdk.application
from core.models import Weather


app_config = {
    "auth": {
        "key": "a-0k740p-6un1ebkdpy",
        "token": "T7(mGuyfFWzPH263)7",
    }
}

client = wiotp.sdk.application.ApplicationClient(config=app_config)

def get_data_device(event):
    data = event.data
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


client.connect()
client.deviceEventCallback = get_data_device
client.subscribeToDeviceEvents()

# import wiotp.sdk.application
#
#
# app_config = {
#     "auth": {
#         "key": "a-0k740p-6un1ebkdpy",
#         "token": "T7(mGuyfFWzPH263)7",
#     }
# }
#
# data_event = {"ti": 0, "to": 0, "tw": 0, "pr": 0, "hi": 0, "ho": 0, "vo": 0, "ra": 0}
#
#
# def event_callback(event):
#     global data_event
#     data_event = event.data
#
#
# def get_data_device():
#     client.deviceEventCallback = event_callback
#     return data_event
#
#
# client = wiotp.sdk.application.ApplicationClient(config=app_config)
# client.connect()
# client.subscribeToDeviceEvents(msgFormat="json")
