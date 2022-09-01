import paho.mqtt.client as paho
import sys
import time

broker="192.168.0.152"
port=1883

topic="cmnd/tasmota_23DFCF/IRsend"
head="{\"Protocol\":\"NEC\",\"Bits\":"
head2="\",\"Data\":"

def on_publish(client,userdata,result):             #create function for callback
    print(f"data published: {result} \n")
    pass

for data in sys.argv[1:] :
    bits = len(data)*4
    msg = head + "\"" + str(bits) + head2 + data + "\"}"
    client1 = paho.Client("control1")                           #create client object
    client1.on_publish = on_publish                          #assign function to callback
    client1.connect(broker,port)                                 #establish connection
    ret = client1.publish(topic,msg)
    print(msg)
    time.sleep(1.0)