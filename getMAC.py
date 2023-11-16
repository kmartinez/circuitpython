# get our Wifi MAC address (for registering)

import wifi

m = [hex(i) for i in wifi.radio.mac_address]

macstring = ""
for macn in m:
    macstring += macn[2:] + ":"

print(macstring)
