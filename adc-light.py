# circuitpython to read an adc
# use IO4 - onboard light sensor
# adc gives a 16bit value but shifted up from 12 hence /16
# prints with brackets so that Mu plotter can plot it
import analogio
import time
from board import *

pin = analogio.AnalogIn(IO4)
while True:
    print((pin.value/16, ))
    time.sleep(0.1)


