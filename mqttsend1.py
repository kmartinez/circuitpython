#!/usr/bin/env python3
# Run this on Win10/Linux/Mac to send a message to the MQTT broker
# change the publish topic for your own message
import paho.mqtt.client as mqtt
broker="srv03183.soton.ac.uk"
port=1883
def on_publish(client,userdata,result):             #create function for callback
    print("data published")
    pass
client1= mqtt.Client("control1")                           #create client object
client1.on_publish = on_publish                          #assign function to callback
client1.connect(broker,port)                                 #establish connection
ret= client1.publish("house/switch","on") 
