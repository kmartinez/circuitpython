# try wifi, print all ssids, connect, ping google
# Uses the traditional secrets.py file for credentials
import wifi
import ipaddress

print("Available WiFi networks:")
for network in wifi.radio.start_scanning_networks():
    print("\t%s\t\tRSSI: %d\tChannel: %d" % (str(network.ssid, "utf-8"),
            network.rssi, network.channel))
wifi.radio.stop_scanning_networks()

# Get wifi secrets
try:
    from secrets import secrets
except ImportError:
    print("WiFi secrets in secrets.py, add them there!")
    raise
print("connencting to ", secrets["ssid"])
wifi.radio.connect(secrets["ssid"], secrets["password"])

googleIP = ipaddress.ip_address("8.8.4.4")
print("Ping google.com: %f ms" % (wifi.radio.ping(googleIP)*1000))
