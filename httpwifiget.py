# simple http get over wifi
# adapted from https://circuitpython.readthedocs.io/projects/imageload/en/latest/examples.html?highlight=requests#requests-test
import ssl
import wifi
import socketpool
import adafruit_requests as requests

# Get wifi secrets
try:
    from secrets import secrets
except ImportError:
    print("WiFi secrets in secrets.py, add them there!")
    raise

wifi.radio.connect(secrets["ssid"], secrets["password"])

print("My IP address is", wifi.radio.ipv4_address)

socket = socketpool.SocketPool(wifi.radio)
https = requests.Session(socket, ssl.create_default_context())

# pylint: disable=line-too-long
url = "http://iotgate.ecs.soton.ac.uk/test/test.txt"

print("Fetching text from %s" % url)
response = https.get(url)
print("GET complete")

print(response.content)


response.close()
