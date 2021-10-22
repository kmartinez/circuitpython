# simple http get over wifi
# adapted from https://circuitpython.readthedocs.io/projects/imageload/en/latest/examples.html?highlight=requests#requests-test
import ssl
import wifi
import socketpool
import adafruit_requests as requests

try:
    from secrets import secrets
except ImportError:
    print("WiFi secrets in secrets.py, add them there!")
    raise

wifi.radio.connect(secrets["ssid"], secrets["password"])

socket = socketpool.SocketPool(wifi.radio)
https = requests.Session(socket, ssl.create_default_context())

jsonurl = "http://iotgate.ecs.soton.ac.uk/test/json.json"
txturl = "http://iotgate.ecs.soton.ac.uk/test/test.txt"
print("Fetching text from %s" % txturl)
response = https.get(txturl)
print("GET complete")
print(response.content)
response = https.get(jsonurl)
print("JSON GET complete")
j = response.json()
print("Value in json: ", j["value"])

response.close()
