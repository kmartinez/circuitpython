# how to use featherS2 -  flash the onboard blue LED
import time
import board
import digitalio

blueled = digitalio.DigitalInOut(board.LED)
blueled.direction = digitalio.Direction.OUTPUT

while True:
    blueled.value = True
    time.sleep(0.5)
    blueled.value = False
    time.sleep(0.5)



