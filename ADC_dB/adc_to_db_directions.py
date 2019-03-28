from machine import I2C, Pin, Timer
import ufirebase as firebase
import ads1x15
import time
#import numpy as np
#import csv
#import math
from struct import unpack as unp
import network
def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect("uofrGuest", "")
        #wlan.connect("SASKTEL0059", "98ce5f13")
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())
do_connect()    
addr = 72
gain = 1
i2c = I2C(scl=Pin(0), sda=Pin(4), freq=400000)
adc = ads1x15.ADS1015(i2c, addr, gain)
#URL = 'noise-c2b8e'
#print(firebase.get(URL))

def north_mic ():
    while True:
        result =adc.read(rate =7, channel1 =3) #Read ADC
        if (result < 893) and (result > 840): #Limiting ADC input to display 35-50
            result=(result-667.1349)/(4.33287) # Converting ADC to dB
            if (result < 52) and (result >38):  # Avoiding false data
                #result = np.float16(result)
                return result
        if (result <925) and (result > 892): #Limiting ADC input to display 50-60
            result=(result-747.2502)/(2.741792)# Converting ADC to dB
            if (result < 64) and (result >52):  # Avoiding false data
                #result = np.float16(result)
                return result            
        if (result <1020) and (result > 924): #Limiting ADC input to display 60-70
            result=(result-145.8678)/(18.3677)# Converting ADC to dB
            if (result < 71) and (result >61):  # Avoiding false data
                #result = np.float16(result)
                return result
        if (result <1200) and (result >1020): #Limiting ADC input to display 70-80
            result=(result+344.078)/(19.00119)# Converting ADC to dB
            if (result < 82) and (result >71):  # Avoiding false data
                #result = np.float16(result)
                return result
        if (result <1600) and (result >1199): #Limiting ADC input to display 80-90
            result=(result+1831.32)/(37.57249)# Converting ADC to dB
            if (result < 93) and (result >79):  # Avoiding false data
                #result = np.float16(result)
                return result
            
 def east_mic ():
    while True:
        result =adc.read(rate =7, channel1 =2) #Read ADC
        if (result < 893) and (result > 840): #Limiting ADC input to display 35-50
            result=(result-667.1349)/(4.33287) # Converting ADC to dB
            if (result < 52) and (result >38):  # Avoiding false data
                #result = np.float16(result)
                return result
        if (result <925) and (result > 892): #Limiting ADC input to display 50-60
            result=(result-747.2502)/(2.741792)# Converting ADC to dB
            if (result < 64) and (result >52):  # Avoiding false data
                #result = np.float16(result)
                return result            
        if (result <1020) and (result > 924): #Limiting ADC input to display 60-70
            result=(result-145.8678)/(18.3677)# Converting ADC to dB
            if (result < 71) and (result >61):  # Avoiding false data
                #result = np.float16(result)
                return result
        if (result <1200) and (result >1020): #Limiting ADC input to display 70-80
            result=(result+344.078)/(19.00119)# Converting ADC to dB
            if (result < 82) and (result >71):  # Avoiding false data
                #result = np.float16(result)
                return result
        if (result <1600) and (result >1199): #Limiting ADC input to display 80-90
            result=(result+1831.32)/(37.57249)# Converting ADC to dB
            if (result < 93) and (result >79):  # Avoiding false data
                #result = np.float16(result)
                return result           
 
def south_mic ():
    while True:
        result =adc.read(rate =7, channel1 =1) #Read ADC
        if (result < 893) and (result > 840): #Limiting ADC input to display 35-50
            result=(result-667.1349)/(4.33287) # Converting ADC to dB
            if (result < 52) and (result >38):  # Avoiding false data
                #result = np.float16(result)
                return result
        if (result <925) and (result > 892): #Limiting ADC input to display 50-60
            result=(result-747.2502)/(2.741792)# Converting ADC to dB
            if (result < 64) and (result >52):  # Avoiding false data
                #result = np.float16(result)
                return result            
        if (result <1020) and (result > 924): #Limiting ADC input to display 60-70
            result=(result-145.8678)/(18.3677)# Converting ADC to dB
            if (result < 71) and (result >61):  # Avoiding false data
                #result = np.float16(result)
                return result
        if (result <1200) and (result >1020): #Limiting ADC input to display 70-80
            result=(result+344.078)/(19.00119)# Converting ADC to dB
            if (result < 82) and (result >71):  # Avoiding false data
                #result = np.float16(result)
                return result
        if (result <1600) and (result >1199): #Limiting ADC input to display 80-90
            result=(result+1831.32)/(37.57249)# Converting ADC to dB
            if (result < 93) and (result >79):  # Avoiding false data
                #result = np.float16(result)
                return result

def west_mic ():
    while True:
        result =adc.read(rate =7, channel1 =0) #Read ADC
        if (result < 893) and (result > 840): #Limiting ADC input to display 35-50
            result=(result-667.1349)/(4.33287) # Converting ADC to dB
            if (result < 52) and (result >38):  # Avoiding false data
                #result = np.float16(result)
                return result
        if (result <925) and (result > 892): #Limiting ADC input to display 50-60
            result=(result-747.2502)/(2.741792)# Converting ADC to dB
            if (result < 64) and (result >52):  # Avoiding false data
                #result = np.float16(result)
                return result            
        if (result <1020) and (result > 924): #Limiting ADC input to display 60-70
            result=(result-145.8678)/(18.3677)# Converting ADC to dB
            if (result < 71) and (result >61):  # Avoiding false data
                #result = np.float16(result)
                return result
        if (result <1200) and (result >1020): #Limiting ADC input to display 70-80
            result=(result+344.078)/(19.00119)# Converting ADC to dB
            if (result < 82) and (result >71):  # Avoiding false data
                #result = np.float16(result)
                return result
        if (result <1600) and (result >1199): #Limiting ADC input to display 80-90
            result=(result+1831.32)/(37.57249)# Converting ADC to dB
            if (result < 93) and (result >79):  # Avoiding false data
                #result = np.float16(result)
                return result
            
def direction (): #compares the dB levels of each microphone and deterimine the direction of the sound
    north1=north_mic()
    east1=east_mic()
    south1=south_mic()
    west1=west_mic()
    
    addNE= (north1 + east1)
    addNW= (north1 + west1)
    addSE= (south1 + east1)
    addSW= (south1 + west1)
    subNE= (north1 - east1)
    subNW= (north1 - west1)
    subSE= (south1 - east1)
    subSW= (south1 - west1)    
    
    ## Checks for N, NE, NW
    if (north1>east1 and north1>south1 and north1>west1): ## checks if north is largest reading
        if (addNE > addNW and addNE > addSW and addNE > addSE):
            if (subNE > -6 and subNE < 6): #Threshold +/- 5dB SPL
                print ("North East")
        if (addNW > addNE and addNW > addSW and addNW > addSE):
            if (subNW > -6 and subNW < 6):
                print ("North West")
        else:
            print ("North")
            
     ## Checks for S, SE, SW
    if (south1>east1 and south1>north1 and south1>west1): ## checks if south is largest reading
        if (addSE > addNW and addSE > addSE and addSE > addSE):
            if (subSE > -6 and subSE < 6): #Threshold +/- 5dB SPL
                print ("South East")
        if (addSW > addNE and addSW > addSW and addSW > addSE):
            if (subSW > -6 and subSW < 6):
                print ("South West")
        else:
            print ("South")
            
     ## Checks for E, NE, SE
    if (east1>south1 and east1>north1 and east1>west1): ## checks if east is largest reading
        if (addSE > addNW and addSE > addSW and addSE > addNE):
            if (subSE > -6 and subSE < 6): #Threshold +/- 5dB SPL
                print ("South East")
        if (addNE > addNW and addNE > addSW and addNE > addSE):
            if (subNE > -6 and subNE < 6):
                print ("North East")
        else:
            print ("East")

     ## Checks for W, NW, SW
    if (west1>south1 and west1>north1 and west1>east1): ## checks if west is largest reading
        if (addSW > addNW and addSW > addSE and addSW > addNE):
            if (subSW > -6 and subSW < 6): #Threshold +/- 5dB SPL
                print ("South West")
        if (addNW > addNE and addNW > addSW and addNW > addSE): 
            if (subNW > -6 and subNW < 6):
                print ("North West")
        else:
            print ("West")



URL = 'noise-c2b8e'
print(firebase.get(URL))
while True:
    #value = adc.read(rate =7, channel1 =0)
    #value = adc.read(rate =7, channel1 =1)
    #value = adc.read(rate =7, channel1 =2)
    #rv = 
    result= conv_to_db()
    #print(conv_to_db())
    firebase.put(URL,{'North':result})
    print (result)
    #firebase.put(URL, {'Mic1': Mic1_Val})
    time.sleep(0.1)


