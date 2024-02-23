# simple example reading an ADC port
# check the comment to choose for S2 light (which is on an adc) or S3
import analogio
import time
from board import *
# featherS2 light sensor
#ADCPORT = IO4
# feather ESP32-S3 adc0
ADCPORT = A0
pin = analogio.AnalogIn(ADCPORT)
while True:
    print((pin.value/16, ))
    time.sleep(0.5)
