# Simple example of reading the MCP3008 analog input channels and printing
# them all out.
# Author: Tony DiCola
# License: Public Domain
#Edited: Abdulaziz Alotaibi
import time

# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import spidev
import os

# Hardware SPI configuration:
SPI_PORT = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))
SPI.max_speed_hz = 1350000

# Main program loop.
while True:
    # Read all the ADC channel values in a list.
    values = [0] * 8
    for i in range(8):
        # The read_adc function will get the value of the specified channel (0-7).
        values[i] = (mcp.read_adc(i) - 600)


    print('{0:>4}'.format(*values))

    time.sleep(0.8)

