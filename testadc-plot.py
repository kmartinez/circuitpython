# test reading an adc
# gives a 16bit value but shifted up from 12
import analogio
import time
from board import *

pin = analogio.AnalogIn(A0)
while True:
    print((pin.value/16, ))
    time.sleep(0.1)


