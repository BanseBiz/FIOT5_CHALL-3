import paho.mqtt.client as paho
import sys
import time

from bleak import BleakClient
from bleak import BleakClient, BleakScanner
from bleak.exc import BleakError

ADDRESS = "ff:21:09:28:32:6c"
CHARACTERISTIC = "0xFFF3"
ON = "0xBC01010155"
OFF = "0xBC01010055"

MQTT_TOPIC = "cmnd/ble"
MQTT_HOST = '192.168.0.152'
MQTT_PORT = 1883

def on_connect(client, userdata, flags, rc):
    print("Connected with result code {0}".format(str(rc)))  


def on_message(client, userdata, msg):
    print("Message received-> " + msg.topic + " " + str(msg.payload))
    if not device:
        raise BleakError(f"A device with address {ADDRESS} could not be found.")
    async with BleakClient(device) as client:
        await client.write_gatt_char(CHARACTERISTIC, bytearray.fromhex(msg.payload))

async def main():
    device = await BleakScanner.find_device_by_address(ADDRESS, timeout=20.0)
    client = mqtt.Client("mqtt_ble_bridge")
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(MQTT_HOST, MQTT_PORT)
    client.loop_forever()

if __name__ == "__main__":
    asyncio.run(main())