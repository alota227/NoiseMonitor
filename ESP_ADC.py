from machine import I2C, Pin, Timer
import ufirebase as firebase
import ads1x15
import time
from struct import unpack as unp
#import network
#def do_connect():
#    wlan = network.WLAN(network.STA_IF)
#    wlan.active(True)
#    if not wlan.isconnected():
#        print('connecting to network...')
#        wlan.connect("uofrGuest", "")
#        #wlan.connect("SASKTEL0059", "98ce5f13")
#        while not wlan.isconnected():
#            pass
#    print('network config:', wlan.ifconfig())
#do_connect()    


addr = 72
gain = 1


i2c = I2C(scl=Pin(0), sda=Pin(4), freq=400000)
adc = ads1x15.ADS1015(i2c, addr, gain)

#
#URL = 'noise-c2b8e'
#print(firebase.get(URL))
#
while True:
    value = adc.read(rate =7, channel1 =0)
    #value = adc.read(rate =7, channel1 =1)
    #value = adc.read(rate =7, channel1 =2)
    #fv =(value-838)/0.658
    fv = value*0.00080586
    #Mic1_Val=value
    #rv = 
    print(value)
    #firebase.put(URL, {'Mic1': Mic1_Val})
    time.sleep(0.5)

