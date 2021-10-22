# handy functions for RGB LED
# not perfect yet
import time
import board
import adafruit_dotstar


class rgbled(object):
    def __init__(self):
        self.led = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
        self.led.brightness = 0.5
    def flash(self):
        self.led.brightness = 1
        time.sleep(0.5)
        self.led.brightness = 0
    def brightness(self, b):
        self.led.brightness = b
    def green(self):
        self.led[0] = (0, 255, 0)
    def blue(self):
        self.led[0] = (0, 0, 255)


myled = rgbled()
myled.blue()
print("blue flash")
myled.flash()
myled.green()
print("green flash")
myled.flash()
while True:
    myled.brightness(0)
    time.sleep(1)
    myled.brightness(1)
