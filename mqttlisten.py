#!/usr/bin/env python3
# Run this on Win10/Linux/Mac to listen for messages from the MQTT broker
# change the subscribe line to listen for your own messages
import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    print("received message: " , str(message.payload.decode("utf-8")))

mqttBroker = "srv03183.soton.ac.uk"

client = mqtt.Client("SimpleListen")
client.connect(mqttBroker)

client.loop_start()

client.subscribe("km/TEMPERATURE")
client.on_message = on_message

time.sleep(30)

client.loop_stop()
