# Simple demo of reading each analog input from the ADS1x15 and printing it to
# the screen.
# Author: Tony DiCola
# License: Public Domain
# Edited: Abdulaziz Alotaibi
import time
# Import the ADS1x15 module.
import Adafruit_ADS1x15
#create an ADS1015 ADC (12-bit) instance.
adc = Adafruit_ADS1x15.ADS1015()


GAIN = 1

print('Reading ADS1x15 values, press Ctrl-C to quit...')
# Print nice channel column headers.
print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*range(4)))

print('-' * 37)
# Main loop.
while True:
    # Read all the ADC channel values in a list.
    values = [0]*4
    for i in range(4):
        # Read the specified ADC channel using the previously set gain value.
        values[i] = adc.read_adc(i, gain=GAIN, data_rate=3300)
        # the ADC conversion time (in samples/second). Each chip has a different
        # set of allowed data rate values, see datasheet Table 9 config register
        # DR bit values.
        #values[i] = adc.read_adc(i, gain=GAIN, data_rate=128)
        # Each value will be a 12 or 16 bit signed integer value depending on the
        # ADC (ADS1015 = 12-bit, ADS1115 = 16-bit).
    # Print the ADC values.
    print('{1:>6}'.format(*values))
    # Pause for half a second.
    time.sleep(0.1)
