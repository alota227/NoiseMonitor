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
def conv_to_db ():
    while True:
        result =adc.read(rate =7, channel1 =0) #Read ADC
        if (result < 893) and (result > 840): #Limiting ADC input to display 35-50
            result=(result-667.1349)/(4.33287) # Converting ADC to dB
            if (result < 52) and (result >38):  # Avoiding false data
                result = np.float16(result)
                return result
        if (result <925) and (result > 892): #Limiting ADC input to display 50-60
            result=(result-747.2502)/(2.741792)# Converting ADC to dB
            if (result < 64) and (result >52):  # Avoiding false data
                result = np.float16(result)
                return result            
        if (result <1020) and (result > 924): #Limiting ADC input to display 60-70
            result=(result-145.8678)/(18.3677)# Converting ADC to dB
            if (result < 71) and (result >61):  # Avoiding false data
                result = np.float16(result)
                return result
        if (result <1200) and (result >1020): #Limiting ADC input to display 70-80
            result=(result+344.078)/(19.00119)# Converting ADC to dB
            if (result < 82) and (result >71):  # Avoiding false data
                result = np.float16(result)
                return result
        if (result <1600) and (result >1199): #Limiting ADC input to display 80-90
            result=(result+1831.32)/(37.57249)# Converting ADC to dB
            if (result < 93) and (result >79):  # Avoiding false data
                result = np.float16(result)
                return result
            
            
            
            
while True:
    #value = adc.read(rate =7, channel1 =0)
    #value = adc.read(rate =7, channel1 =1)
    #value = adc.read(rate =7, channel1 =2)
    #fv =(value-838)/0.658
    fv = value*0.00080586
    #Mic1_Val=value
    #rv = 
    result=def conv_to_db ()
    print(result)
    #firebase.put(URL, {'Mic1': Mic1_Val})
    time.sleep(0.5)

