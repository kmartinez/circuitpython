# send data MQTT to our VM
# Change the mqtt_topic to yourID/temperature
# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
import ssl
import socketpool
import wifi
import adafruit_minimqtt.adafruit_minimqtt as MQTT
from time import sleep

# pylint: disable=no-name-in-module,wrong-import-order
try:
    from secrets import secrets
except ImportError:
    print("WiFi secrets are kept in secrets.py, please add them there!")
    raise

print("Connecting to %s" % secrets["ssid"])
wifi.radio.connect(secrets["ssid"], secrets["password"])
print("Connected to %s!" % secrets["ssid"])

### Topic Setup ###
mqtt_topic = "km/temperature"

# Define callback methods which are called when events occur
# pylint: disable=unused-argument, redefined-outer-name
def connect(mqtt_client, userdata, flags, rc):
    # This will be called when the mqtt_client is connected successfully to the broker.
    print("Connected to MQTT Broker")
    print("Flags: {0}\n RC: {1}".format(flags, rc))


def disconnect(mqtt_client, userdata, rc):
    # called when the mqtt_client disconnects
    print("Disconnected from MQTT Broker!")

def publish(mqtt_client, userdata, topic, pid):
    # This method is called when the mqtt_client publishes data to a feed.
    print("Published to {0} with PID {1}".format(topic, pid))

# Create a socket pool
pool = socketpool.SocketPool(wifi.radio)

# Set up a MiniMQTT Client
mqtt_client = MQTT.MQTT(
    #broker="srv03183.soton.ac.uk",
    broker="192.168.175.4",
    port=1883,
    username="none",
    password="non",
    socket_pool=pool,
    ssl_context=ssl.create_default_context(),
)

# Connect callback handlers to mqtt_client
mqtt_client.on_connect = connect
mqtt_client.on_disconnect = disconnect
mqtt_client.on_publish = publish

print("Attempting to connect to %s" % mqtt_client.broker)
mqtt_client.connect()

print("Publishing to %s" % mqtt_topic)
count = 10
while count != 0 :
    reading = str(count + 20.0)
    mqtt_client.publish(mqtt_topic, reading)
    count = count - 1
    sleep(1)

print("Disconnecting from %s" % mqtt_client.broker)
mqtt_client.disconnect()
