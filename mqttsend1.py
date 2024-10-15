#!/usr/bin/env python3
# Run this to send a message to a MQTT broker
# change the publish topic to your own message eg username/
# adapted from paho-mqtt publisher example
# you need pip3 install paho-mqtt
import paho.mqtt.client as mqtt
import time

broker = "srv03183.soton.ac.uk"

def on_publish(client, userdata, mid, reason_code, properties):
    try:
        userdata.remove(mid)
    except KeyError:
        print("some error ocurred")

unacked_publish = set()
mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.on_publish = on_publish

mqttc.user_data_set(unacked_publish)
mqttc.connect(broker)
mqttc.loop_start()

# Our application produce some messages
msg_info = mqttc.publish("username/topic", "a test message", qos=1)
unacked_publish.add(msg_info.mid)

# Wait for all message to be published
while len(unacked_publish):
    time.sleep(0.1)

# Due to race-condition the following way to wait for all publish is safer
msg_info.wait_for_publish()

mqttc.disconnect()
mqttc.loop_stop()