import asyncio
import time

from bleak import BleakClient
from bleak import BleakClient, BleakScanner
from bleak.exc import BleakError

ADDRESS = "ff:21:09:28:32:6c"
CHARACTERISTIC = "0xfff3"
ON = "0xBC01010155"
OFF = "0xBC01010055"


async def main():
    device = await BleakScanner.find_device_by_address(ADDRESS, timeout=20.0)
    if not device:
        raise BleakError(f"A device with address {ADDRESS} could not be found.")
    async with BleakClient(device) as client:
        #await client.write_gatt_char(CHARACTERISTIC, OFF)
        #time.sleep(2.0)
        #await client.write_gatt_char(CHARACTERISTIC, ON)
        svcs = await client.get_services()
        print("Services:")
        for service in svcs:
            print(service)


if __name__ == "__main__":
    asyncio.run(main())