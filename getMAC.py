# try wifi, get mac

import wifi
def formatmac(mac):
    smac = ""
    for ot in list(mac):
        h = hex(ot)
        smac += h[2] + h[3]
    return(smac)

# Get wifi secrets
try:
    from secrets import secrets
except ImportError:
    print("WiFi secrets in secrets.py, add them there!")
    raise

wifi.radio.connect(secrets["ssid"], secrets["password"])

print("My IP address is", wifi.radio.ipv4_address)
mac = wifi.radio.mac_address
#smac = ""
#for ot in list(mac):
#    h = hex(ot)
#    smac += h[2] + h[3]
smac = formatmac(mac)
print("MAC: ", smac)
