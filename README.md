Circuitpython for the featherS2 boards used in ECS modules
Basics:  
simpleLED - onboard blue LED  
rgbled - onboard RGB led  
memfree - shows space in flash/ram  
myled - simpler class for rgb   
test-myled - tests above  

testadc-plot - simple adc channel reads  
adc-light - do something with onboard light sensor  

QWIIC Sensors:  
aht20  
sensor9809  

Other features:  
 deep-sleep - use alarm to deep sleep and cold-wake

Wifi and networking:  
trywifi - link to wifi (using secrets.py)  
wificonnect - keeps wifi on in case it drops
wifi-http-get - fetch data from the web  
mqtt-sender - send message to a broker  
openweather - shows how to get data from weather API  

Code for linux/win10:  
mqttlisten - listener for mqtt messages  
mqttsend1 - send a message to broker  
