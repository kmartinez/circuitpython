"""
test with TMP117 temp sensor and a plug-on screen
uses average of 8 readings in their driver
"""

import board
import displayio
import terminalio
from adafruit_display_text import label
import adafruit_displayio_sh1107
import time
from adafruit_tmp117 import TMP117, AverageCount

i2c = board.I2C()  # uses board.SCL and board.SDA
tmp117 = TMP117(i2c)
tmp117.averaged_measurements = AverageCount.AVERAGE_8X

displayio.release_displays()
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
display = adafruit_displayio_sh1107.SH1107(
    display_bus, width=128, height=64, rotation=0
)

# Setup the display
splash = displayio.Group()
display.show(splash)
text_area = label.Label(terminalio.FONT, text="init", scale=1, color=0xFFFFFF, x=8, y=44
)
def pscreen(t):
    text_area.text = t
    display.show(text_area)

# if permanent offset needed: tmp117.temperature_offset = 1.0
while True:
    print(tmp117.temperature)
    pscreen("        ")
    pscreen(str(tmp117.temperature))
    time.sleep(1)