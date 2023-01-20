# connect to wifi if we haven't
# in case of very long running where you need a connection and it may drop
# uses the typical secrets.py for name/pass
import wifi, ipaddress
from time import sleep

def connectwifi():
    ipv4 = ipaddress.ip_address("192.168.1.1")
    if wifi.radio.ping(ipv4) == None:
        try:
            from secrets import secrets
            print("connecting to ",secrets["ssid"] )
            wifi.radio.connect(secrets["ssid"], secrets["password"])
         
        except ImportError:
            print("WiFi secrets needed in secrets.py")
            raise

while True:
    connectwifi()
    print("we're still connected")
    sleep(2)
