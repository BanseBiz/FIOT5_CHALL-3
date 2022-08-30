import paho.mqtt.client as paho
import sys
import time

broker="192.168.0.234"
port=1883

topic="cmnd/tasmota_23DFCF"


def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")
    pass

for cmnd in sys.argv[1:] :
    client1 = paho.Client("control1")                           #create client object
    client1.on_publish = on_publish                          #assign function to callback
    client1.connect(broker,port)                                 #establish connection
    ret = client1.publish(topic,cmnd)
    print(cmnd)
    time.sleep(0.8)