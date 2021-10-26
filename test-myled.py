# handy functions for RGB LED
# not perfect yet
import time
import board
import adafruit_dotstar
from myled import rgbled

led = rgbled()

while True:
    led.green()
    time.sleep(1)
    led.red()
    time.sleep(1)
    led.off()
    time.sleep(1)
