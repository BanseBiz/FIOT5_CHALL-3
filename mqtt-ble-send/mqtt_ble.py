import paho.mqtt.client as mqtt
import sys
import time
import asyncio
import threading
import json

from bleak import BleakClient
from bleak import BleakClient, BleakScanner
from bleak.exc import BleakError

#ADDRESS = "ff:21:09:28:32:6c"
#ADDRESS = "ff:21:09:28:22:5a"
#CHARACTERISTIC = "0000fff3-0000-1000-8000-00805f9b34fb"

CONFIG_PATH = '/home/fiot5/FIOT_CHALL-5/CONFIGS/mqtt_ble_config.json'
COMMANDS_PATH = '/home/fiot5/FIOT_CHALL-5/CONFIGS/jtx_commands.json'

ble_commands = []

def on_connect(client, userdata, flags, rc):
    print("Connected with result code {0}".format(str(rc)))


def on_message(client, userdata, msg):
    print("Message received-> " + msg.topic + " " + str(msg.payload.decode("utf-8")))
    ble_commands.append(msg.payload.decode("utf-8"))

def ble_command_thread():
    asyncio.run(ble_command_handle())

async def ble_command_handle():
    while 1:
        if ble_commands:
            with open(COMMANDS_PATH) as f:
                ble_commands_list = json.loads(f.read())
                f.close()
                print("Connecting to ble device")
                with open(CONFIG_PATH) as conf_f:
                    config = json.loads(conf_f.read())
                    address = config["BLE_ADDRESS"]
                    characteristic = config["CHARACTERISTIC"]
                    try: 
                        device = await BleakScanner.find_device_by_address(address, timeout=20.0)
                        if not device:
                            print(f"a device with address {address} could not be found.")
                        async with BleakClient(device) as client:
                            await client.write_gatt_char(characteristic, bytearray.fromhex(ble_commands_list[ble_commands.pop(0)]))
                            print(f"send command to ble device")
                        conf_f.close()
                    except:
                        print("Ohh no, an exception occurred. That's sad")
        await asyncio.sleep(2.0)
    return 1


async def main():   
    with open(CONFIG_PATH) as conf_f:
        config = json.loads(conf_f.read())
        topic = config["MQTT_LISTEN_TOPIC"]
        mqtt_host = config["MQTT_HOST"]
        mqtt_port = int(config["MQTT_PORT"])
        conf_f.close()    

        ble_thread = threading.Thread(target=ble_command_thread)
        ble_thread.start()
        client = mqtt.Client("mqtt_ble_bridge")
        client.on_connect = on_connect
        client.on_message = on_message
        client.connect(mqtt_host, mqtt_port)
        client.subscribe(topic,0)
        client.loop_forever()

if __name__ == "__main__":
    asyncio.run(main())