# -*- coding: utf-8 -*-
import wiotp.sdk.device
import time


config = {
    "identity": {
        "orgId": "0k740p",
        "typeId": "Esp8266",
        "deviceId": "seradya",
    },
    "auth": {
        "token": "NDdVf07KBd2vjL(e6d",
    }
}

def myCommandCallback(cmd):
    print("Command received: %s" % cmd.data)

# Configure
client = wiotp.sdk.device.DeviceClient(config=config, logHandlers=None)
client.commandCallback = myCommandCallback

# # Connect
# device1.connect()
#
# # Send Data
# myData={'ti' : 50}
# device1.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
#
# # Disconnect
# device1.disconnect()
