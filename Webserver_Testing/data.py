from machine import I2C, Pin, Timer
import ufirebase as firebase
import ads1x15
from struct import unpack as unp
import network
from firebase import firebase
import time
import os
import datetime
import urllib.request
import urllib.parse
from time import strftime


firebase = firebase.FirebaseApplication('https://noise-c2b8e.firebaseio.com/', None)

def direction (north1,east1,south1,west1): #compares the dB levels of each microphone and deterimine the direction of the sound
    
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
        if ((addSE > addNW) and (addSE > addSE) and (addSE > addSE) and (subSE > -6 and subSE < 6)):
            print ("South East")
        elif ((addSW > addNE) and (addSW > addSW) and (addSW > addSE) and (subSW > -6 and subSW < 6)):
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

     Checks for W, NW, SW
   if (west1>south1 and west1>north1 and west1>east1): ## checks if west is largest reading
       if ((addSW > addNW) and (addSW > addSE) and (addSW > addNE) and (subSW > -6 and subSW < 6)):
           print ("South West")
       elif ((addNW > addNE) and (addNW > addSW) and (addNW > addSE) and (subNW > -6 and subNW < 6) ): 
           print ("North West")
       else:
           print ("West")
		   
def average(n,e,s,w):
    return ((int(n)+int(e)+int(s)+int(w))/4.0)
    
while True:
    result = firebase.get('/',None)
    print (result)

    temperature=firebase.get('/temperature',None)
    print ('Temperature: '+str(temperature))

    humidity=firebase.get('/humidity',None)
    print ('Humidity: '+str(humidity))
    
    oneNorth=firebase.get('/North',None)
    print ('MIC1: '+ str(oneNorth))
    
    east=firebase.get('/East',None)
    print ('MIC2: '+ str(east))
 
    south=firebase.get('/South',None)
    print ('MIC3: '+ str(south))
    
    west=firebase.get('/West',None)
    print ('MIC4: '+ str(west))
    
    ave = average(oneNorth,east,south,west)
    avg = str(ave)
    print(avg)
    
	dir= direction(oneNorth,east,south,west)
	print(dir)
	
    dt = datetime.datetime.now().strftime('%Y-%m-%d %H"%M:%S')
    #dt.datetime.now(gettz("Europe/Madrid")).isoformat()
    print (dt)
    
    temp = "%.1f" %temperature
    hum = "%.1f" %humidity
    
    data = {}
    data['dt'] = dt
    data['temp'] = temp
    data['hum'] = hum
    data['oneNorth'] = oneNorth
    data['oneEast'] = east
    data['oneSouth'] = south
    data['oneWest'] = west
    data['spl'] = avg
	data['dir' = dir
    
    url_values = urllib.parse.urlencode(data)
    print(url_values)
    url = 'https://www.m0nitorsystem.com/add_data.php'
    full_url = url + '?' + url_values
    data = urllib.request.urlopen(full_url)
    print ('------------')
	

       
