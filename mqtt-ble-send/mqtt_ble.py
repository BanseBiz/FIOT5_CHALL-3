import paho.mqtt.client as mqtt
import sys
import time
import asyncio
import threading
import json

from bleak import BleakClient
from bleak import BleakClient, BleakScanner
from bleak.exc import BleakError

ADDRESS = "ff:21:09:28:32:6c"
CHARACTERISTIC = "0000fff3-0000-1000-8000-00805f9b34fb"
ON = "0xBC01010155"
OFF = "0xBC01010055"

MQTT_TOPIC = "cmnd/ble"
MQTT_HOST = '192.168.0.152'
MQTT_PORT = 1883

ble_commands = []
ble_commands_list = []

def on_connect(client, userdata, flags, rc):
    print("Connected with result code {0}".format(str(rc)))


def on_message(client, userdata, msg):
    print("Message received-> " + msg.topic + " " + str(msg.payload))
    ble_commands.append(ble_commands_list[msg.payload])

def ble_command_thread():
    asyncio.run(ble_command_handle())

async def ble_command_handle():
    while 1:
        if ble_commands:
            print("Connecting to ble device")
            device = await BleakScanner.find_device_by_address(ADDRESS, timeout=20.0)
            if not device:
                print(f"a device with address {ADDRESS} could not be found.")
            async with BleakClient(device) as client:
                await client.write_gatt_char(CHARACTERISTIC, ble_commands.pop(0))
                print(f"send command to ble device")
        await asyncio.sleep(2.0)
    return 1


async def main():
    with open('jtx_commands.json') as f:
        ble_commands_list = json.loads(f.read())
        f.close()
    
    ble_thread = threading.Thread(target=ble_command_thread)
    ble_thread.start()
    client = mqtt.Client("mqtt_ble_bridge")
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(MQTT_HOST, MQTT_PORT)
    client.subscribe(MQTT_TOPIC,0)
    client.loop_forever()

if __name__ == "__main__":
    asyncio.run(main())