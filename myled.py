# handy functions for RGB LED
# usage: from myled import rgbled then make something like led = rgbled()
import board
import adafruit_dotstar

class rgbled(object):
    def __init__(self):
        self.led = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
        self.led.brightness = 0.3
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
    def red(self):
        self.led[0] = (200, 0, 0)
    def off(self):
        self.led[0] = (0,0,0)


