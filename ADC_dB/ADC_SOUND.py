# Simple demo of reading each analog input from the ADS1x15 and printing it to
# the screen.
# Author: Tony DiCola
# Edited by: Abdulaziz Alotaibi / University of Regina 2019
# License: Public Domain
import time
import numpy as np
import Adafruit_ADS1x15
import csv
import math

# Create an ADS1115 ADC (16-bit) instance.
#adc = Adafruit_ADS1x15.ADS1115()

# Or create an ADS1015 ADC (12-bit) instance.
adc = Adafruit_ADS1x15.ADS1015()

# Note you can change the I2C address from its default (0x48), and/or the I2C
# bus by passing in these optional parameters:
#adc = Adafruit_ADS1x15.ADS1015(address=0x49, busnum=1)

# Choose a gain of 1 for reading voltages from 0 to 4.09V.# Or pick a different gain to change the range of voltages that are read:
#  - 2/3 = +/-6.144V
#  -   1 = +/-4.096V
#  -   2 = +/-2.048V
#  -   4 = +/-1.024V
#  -   8 = +/-0.512V
#  -  16 = +/-0.256V
GAIN = 1

print('Reading ADS1x15 values, press Ctrl-C to quit...')
#with open("dB_Values22.cvs", "w") as out_file

def conv_db_quad ():
    while True:
        result =adc.read_adc(0, gain=GAIN, data_rate=3300)
        #if (result < 1350) and (result > 1100):

def db_quad():
    while True:
        result =adc.read_adc(0, gain=GAIN, data_rate=3300)
        if (result<2500) and (result > 1332.2):
            result = (27.0558+(math.sqrt(1.09702*result-1461.25797)))/(0.54851)
            if (result < 100) and (result > 35):
                return result
def conv_db ():
    while True:
        result =adc.read_adc(0, gain=GAIN, data_rate=3300)
        if (result < 1363) and (result > 1230):
            result=(result-990.8196)/(6.163967)
            if (result < 62) and (result >35):  
                return result
        if (result <1500) and (result > 1390):
            result=(result-150.0336)/(19.1704)
            if (result < 72) and (result >61):  
                return result            
        if (result <1621) and (result > 1520):
            result=(result-145.8678)/(18.3677)
            if (result < 82) and (result >71):  
                return result
        if (result <1940) and (result >1621):
            result=(result+902.623)/(31.10444)
            if (result < 99) and (result >81):  
                return result
##dataset=open("dataset55555.csv", "w")
##def write_data():
##    obj=csv.writer(dataset)
##    obj.writerow([db_value()])
##
##while True:
##    write_data()
##dataset.close()

while True:
    
    #res =db_value()
    #read_adc_ch0 =adc.read_adc(0, gain=GAIN,data_rate=3300)
    print conv_db()
    #print db_value()
    #print read_adc_ch0
    time.sleep(0.5)
