from machine import I2C, Pin, Timer
import ufirebase as firebase
import ads1x15
import time
from struct import unpack as unp
import network


addr = 72
gain = 1


i2c = I2C(scl=Pin(0), sda=Pin(4), freq=400000)
adc = ads1x15.ADS1015(i2c, addr, gain)

#
#URL = 'noise-c2b8e'
#print(firebase.get(URL))
#
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
        if ((addNE > addNW) and (addNE > addSW) and (addNE > addSE ) and (subNE > -6 and subNE < 6)):
            print ("North East")
        elif ((addNW > addNE) and (addNW > addSW) and (addNW > addSE) and (subNW > -6 and subNW < 6)):
            print ("North West")
        else:
            print ("North")
            
     ## Checks for S, SE, SW
    if (south1>east1 and south1>north1 and south1>west1): ## checks if south is largest reading
        if ((addSE > addNW) and (addSE > addNE) and (addSE > addSW) and (subSE > -6 and subSE < 6)):
            print ("South East")
        elif ((addSW > addNE) and (addSW > addNW) and (addSW > addSE) and (subSW > -6 and subSW < 6)):
            print ("South West")
        else:
            print ("South")
            
     ## Checks for E, NE, SE
    if (east1>south1 and east1>north1 and east1>west1): ## checks if east is largest reading
        if ((addSE > addNW) and (addSE > addSW) and (addSE > addNE) and (subSE > -6 and subSE < 6)):
            print ("South East")
        elif ((addNE > addNW) and (addNE > addSW) and (addNE > addSE) and (subNE > -6 and subNE < 6)):
            print ("North East")
        else:
            print ("East")

     ## Checks for W, NW, SW
    if (west1>south1 and west1>north1 and west1>east1): ## checks if west is largest reading
        if ((addSW > addNW) and (addSW > addSE) and (addSW > addNE) and (subSW > -6 and subSW < 6)):
            print ("South West")
        elif ((addNW > addNE) and (addNW > addSW) and (addNW > addSE) and (subNW > -6 and subNW < 6) ): 
            print ("North West")
        else:
            print ("West")

            
            
#URL = 'noise-c2b8e'
#print(firebase.get(URL))
while True:

        
    result= south_mic()
    result2= north_mic()
    result3= west_mic()
    result4 = east_mic()
        #firebase.put(URL,{'West':result, 'South':resultS})
        #firebase.put(URL,{'South':resultS})
        #firebase.put(URL,{'West':result})
    print (result)
    print(result2)
    print(result3)
    print(result4)
    dir= direction()


        #print("-------------------")
        #firebase.put(URL, {'Mic1': Mic1_Val})
    time.sleep(0.5)


    #value = adc.read(rate =7, channel1 =0)
#    value = adc.read(rate =7, channel1 =1)
    #value = adc.read(rate =7, channel1 =2)
    #rv = 
#    result= conv_to_db()
#    #print(conv_to_db())
#    firebase.put(URL,{'North':result})
#    print (value)
#    #firebase.put(URL, {'Mic1': Mic1_Val})
#    time.sleep(0.1)
