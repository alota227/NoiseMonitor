#!/usr/bin/python
import time
import os
import datetime
import requests
import urllib
import threading
from time import strftime
import paho.mqtt.client as mqtt

#while 1:
def sendDataToServer():
    dt = datetime.datetime.now().strftime('%Y-%m-%d %H"%M:%S')
    print (dt)
    print('{0}°C {1}%'.format(t, h))
    urllib.urlopen("http://www.m0nitorsystem.com/add_data.php?dt="+dt+"&t="+t+"&h="+h).read()


    # Callback fires when conected to MQTT broker.
def on_connect(client, userdata, flags, rc):
    print('Connected with result code {0}'.format(rc))
    # Subscribe (or renew if reconnect).
    client.subscribe('Node_1')


# Callback fires when a published message is received.
def on_message(client, userdata, msg):
    # Decode temperature and humidity values from binary message paylod.
    t,h = [float(x) for x in msg.payload.decode("utf-8").split(',')]
    sendDataToServer()  # Display data on webpage


client = mqtt.Client()
client.on_connect = on_connect  # Specify on_connect callback
client.on_message = on_message  # Specify on_message callback
client.connect('localhost', 1883, 60)  # Connect to MQTT broker (also running on Pi).

# Processes MQTT network traffic, callbacks and reconnections. (Blocking)
client.loop_forever()
#time.sleep(1)

