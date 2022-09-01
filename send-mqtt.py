import paho.mqtt.client as paho
import sys
import time

broker="192.168.0.152"
port=1883

def on_publish(client,userdata,result):
    print(f"data published: {result} \n")
    pass

topic = sys.argv[1]

print(f"Publishing on topic {topic}")

for data in sys.argv[2:] :
    client1 = paho.Client("control1")
    client1.on_publish = on_publish
    client1.connect(broker,port)
    ret = client1.publish(topic,data)
    print(data)