#!/usr/bin/env python3
# Run this to listen for messages from a MQTT broker
# change the subscribe line to listen for your own messages
# you need pip3 install paho-mqtt
# adapted from subscriber example from paho-mqtt
import paho.mqtt.client as mqtt
import time

broker = "srv03183.soton.ac.uk"

def on_message(client, userdata, message):
    print("received message: " , str(message.payload.decode("utf-8")))

def on_subscribe(client, userdata, mid, reason_code_list, properties):
    # Since we subscribed only for a single channel, reason_code_list contains
    # a single entry
    if reason_code_list[0].is_failure:
        print(f"Broker rejected you subscription: {reason_code_list[0]}")
    else:
        print(f"Broker granted the following QoS: {reason_code_list[0].value}")

def on_unsubscribe(client, userdata, mid, reason_code_list, properties):
    # Be careful, the reason_code_list is only present in MQTTv5.
    # In MQTTv3 it will always be empty
    if len(reason_code_list) == 0 or not reason_code_list[0].is_failure:
        print("unsubscribe succeeded (if SUBACK is received in MQTTv3 it success)")
    else:
        print(f"Broker replied with failure: {reason_code_list[0]}")
    client.disconnect()

def on_message(client, userdata, message):
    # userdata is the structure we choose to provide, here it's a list()
    userdata.append(message.payload)
    # We only want to process 1 message - can be changed to more
    if len(userdata) >= 0:
        client.unsubscribe("$SYS/#")

def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code.is_failure:
        print(f"Failed to connect: {reason_code}. loop_forever() will retry connection")
    else:
        # CHANGE THIS TOPIC TO YOURS
        client.subscribe("username/topic")

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.on_connect = on_connect
mqttc.on_message = on_message
mqttc.on_subscribe = on_subscribe
mqttc.on_unsubscribe = on_unsubscribe

mqttc.user_data_set([])
mqttc.connect(broker)
mqttc.loop_forever()
print(f"Received the following message: {mqttc.user_data_get()}")
