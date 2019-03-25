from firebase import firebase
import time
import os
import datetime
import urllib.request
import urllib.parse
from time import strftime
#from dateutil.tz import gettz

firebase = firebase.FirebaseApplication('https://noise-c2b8e.firebaseio.com/', None)

def average(n,e,s,w):
    return ((int(n)+int(e)+int(s)+int(w))/4.0)
    
while True:
    result = firebase.get('/',None)
    print (result)

    temperature=firebase.get('/temperature',None)
    print ('Temperature: '+str(temperature))

    humidity=firebase.get('/humidity',None)
    print ('Humidity: '+str(humidity))
    
    north=firebase.get('/North',None)
    print ('MIC1: '+ north)
    
    east=firebase.get('/East',None)
    print ('MIC2: '+ east)
    
    south=firebase.get('/South',None)
    print ('MIC3: '+ south)
    
    west=firebase.get('/West',None)
    print ('MIC4: '+ west)
    
    ave = average(north,east,south,west)
    avg = str(ave)
    print(avg)
    
    dt = datetime.datetime.now().strftime('%Y-%m-%d %H"%M:%S')
    #dt.datetime.now(gettz("Europe/Madrid")).isoformat()
    print (dt)
    
    temp = "%.1f" %temperature
    hum = "%.1f" %humidity
    
    data = {}
    data['dt'] = dt
    data['temp'] = temp
    data['hum'] = hum
    data['oneNorth'] = north
    data['oneEast'] = east
    data['oneSouth'] = south
    data['oneWest'] = west
    data['spl'] = avg
    
    url_values = urllib.parse.urlencode(data)
    print(url_values)
    url = 'https://www.m0nitorsystem.com/add_data.php'
    full_url = url + '?' + url_values
    data = urllib.request.urlopen(full_url)
    print ('------------')
    
    
    
    time.sleep(2)