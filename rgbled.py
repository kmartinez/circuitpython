# how to use onboard RGB LED
# the led values are (red,green,blue)
# check if you have a neopixel (like on S3) or APA102 (like on S2)
from time import sleep
import board
import adafruit_dotstar

led = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
# version for Feather S3
#led = neopixel.NeoPixel(board.NEOPIXEL, 1)
led.brightness = 0.2
    
while True:
    led[0] = (255, 0, 0)
    sleep(0.5)
    led[0] = (0, 255, 0)
    sleep(0.5)
    led[0] = (0, 0, 255)
    sleep(0.5)
