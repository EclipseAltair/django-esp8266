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
    data_device = event.data
    print(data_device)
    w = Weather(
        temp_in=data_device['ti'],
        temp_out=data_device['to'],
        temp_water=data_device['tw'],
        pressure=data_device['pr'],
        humidity_in=data_device['hi'],
        humidity_out=data_device['ho'],
        voltage=data_device['vo'],
        rain=data_device['ra']
    )
    w.save()


client.connect()
client.deviceEventCallback = get_data_device
client.subscribeToDeviceEvents(msgFormat="json")
