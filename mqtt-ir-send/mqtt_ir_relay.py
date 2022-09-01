import paho.mqtt.client as mqtt
import sys
import time
import json
import asyncio

CONFIG_PATH = '../CONFIGS/mqtt_ir_relay_config.json'
COMMANDS_DMX_PATH = '../CONFIGS/DMX_commands.json'
COMMANDS_LED_PATH = '../CONFIGS/LDEstrip_commands.json'

HEAD="{\"Protocol\":\"NEC\",\"Bits\":"
HEAD2="\",\"Data\":"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code {0}".format(str(rc)))


def on_message(client, userdata, msg):
    print("Message received-> " + msg.topic + " " + str(msg.payload.decode("utf-8")))
    with open(COMMANDS_LED_PATH) as led_f:
        with open(COMMANDS_DMX_PATH) as dmx_f:
            led_commands = json.loads(led_f.read())
            dmx_commands = json.loads(dmx_f.read())
            with open(CONFIG_PATH) as conf_f:
                config = json.loads(conf_f.read())
                pub_topic = config["MQTT_PUBLISH_TOPIC"]
                mqtt_host = config["MQTT_HOST"]
                mqtt_port = int(config["MQTT_PORT"])
                conf_f.close()
                sender = mqtt.Client("mqtt_ir_bridge_sender")
                sender.connect(mqtt_host, mqtt_port)

                try:
                    data = led_commands[str(msg.payload.decode("utf-8"))]
                    bits = len(data)*4
                    msg_pub = HEAD + "\"" + str(bits) + HEAD2 + data + "\"}"
                    sender.publish(pub_topic,msg_pub)
                except KeyError:
                    print("Key unknown for led")
                
                try:
                    data = dmx_commands[str(msg.payload.decode("utf-8"))]
                    bits = len(data)*4
                    msg_pub = HEAD + "\"" + str(bits) + HEAD2 + data + "\"}"
                    sender.publish(pub_topic,msg_pub)
                except KeyError:
                    print("Key unknown for dmx")

                print("published")
            dmx_f.close()
        led_f.close()
    

async def main():   
    with open(CONFIG_PATH) as conf_f:
        config = json.loads(conf_f.read())
        sub_topic = config["MQTT_LISTEN_TOPIC"]
        mqtt_host = config["MQTT_HOST"]
        mqtt_port = int(config["MQTT_PORT"])
        conf_f.close()    

        client = mqtt.Client("mqtt_ir_bridge")
        client.on_connect = on_connect
        client.on_message = on_message
        client.connect(mqtt_host, mqtt_port)
        client.subscribe(sub_topic,0)
        client.loop_forever()

if __name__ == "__main__":
    asyncio.run(main())