# http get over wifi - of openweather
# You need to sign up to get your own key
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
socket = socketpool.SocketPool(wifi.radio)
https = requests.Session(socket, ssl.create_default_context())

#jsonurl = "http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=814922d4aa47549f372f484f999d2600"
# local cached copy (you need to use your own APPID for openweathermap)
jsonurl = "http://iotgate.ecs.soton.ac.uk/test/weather.json"

response = https.get(jsonurl)
print("GET complete")
j = response.json()
#we want the main section
t = j["main"]
print(float(t["temp"]) -273.15)
# -273.15 to convert from Kelvin

response.close()
