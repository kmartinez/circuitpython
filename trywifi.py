# try wifi, get mac, ping google
# Uses the traditional secrets.py file for credentials
import wifi
import ipaddress

def formatmac(mac):
    smac = ""
    for ot in list(mac):
        h = hex(ot)
        smac += h[2] + h[3]
    return(smac)

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

print("My IP address is", wifi.radio.ipv4_address)
mac = wifi.radio.mac_address

print("my MAC: ", formatmac(mac))

googleIP = ipaddress.ip_address("8.8.4.4")
print("Ping google.com: %f ms" % (wifi.radio.ping(googleIP)*1000))
