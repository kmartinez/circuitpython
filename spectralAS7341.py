# adapted from SPDX-FileCopyrightText: 2020 Bryan Siepert, written for Adafruit Industries
# SPDX-License-Identifier: MIT
# multi-spectral sensor tester
from time import sleep
import board
from adafruit_as7341 import AS7341

i2c = board.I2C()  # uses board.SCL and board.SDA
sensor = AS7341(i2c)

def bar_graph(read_value):
    scaled = int(read_value / 1000)
    return "[%5d] " % read_value + (scaled * "*")

while True:
    print("415nm/Violet  %s" % bar_graph(sensor.channel_415nm))
    print("445nm//Indigo %s" % bar_graph(sensor.channel_445nm))
    print("480nm//Blue   %s" % bar_graph(sensor.channel_480nm))
    print("515nm//Cyan   %s" % bar_graph(sensor.channel_515nm))
    print("555nm/Green   %s" % bar_graph(sensor.channel_555nm))
    print("590nm/Yellow  %s" % bar_graph(sensor.channel_590nm))
    print("630nm/Orange  %s" % bar_graph(sensor.channel_630nm))
    print("680nm/Red     %s" % bar_graph(sensor.channel_680nm))
    #print("Clear              %s" % bar_graph(sensor.channel_clear))
    print("Near-IR (NIR)      %s" % bar_graph(sensor.channel_nir))
    print("\n------------------------------------------------")
    sleep(1)
