import asyncio
import time

from bleak import BleakClient
from bleak import BleakClient, BleakScanner
from bleak.exc import BleakError

ADDRESS = "ff:21:09:28:32:6c"
CHARACTERISTIC = "0000fff3-0000-1000-8000-00805f9b34fb"
ON = "0xBC01010155"
OFF = "0xBC01010055"


async def main():
    device = await BleakScanner.find_device_by_address(ADDRESS, timeout=20.0)
    if not device:
        raise BleakError(f"A device with address {ADDRESS} could not be found.")
    async with BleakClient(device) as client:
        svcs = await client.get_services()
        print("Services:")
        for service in svcs:
            print(service)
            for char in service.characteristics:
                print("Characteristic:")
                print(char)
        await client.write_gatt_char(CHARACTERISTIC, OFF)
        time.sleep(2.0)
        await client.write_gatt_char(CHARACTERISTIC, ON)


if __name__ == "__main__":
    asyncio.run(main())