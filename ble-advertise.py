import time
from adafruit_ble import BLERadio
from adafruit_ble_beacon import iBeaconAdvertisement

ble = BLERadio()

advertisement = iBeaconAdvertisement()
advertisement.uuid = b"CircuitPython123"
advertisement.major = 1
advertisement.minor = 32
advertisement.beacon_tx_power = -80

while True:
    ble.start_advertising(advertisement)
    time.sleep(10)
    ble.stop_advertising()
    time.sleep(3)
