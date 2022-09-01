import asyncio
import time
import json
import sys

from bleak import BleakClient
from bleak import BleakClient, BleakScanner
from bleak.exc import BleakError

ADDRESS = "ff:21:09:28:32:6c"
CHARACTERISTIC = "0000fff3-0000-1000-8000-00805f9b34fb"
ON = "bc01010155"
OFF = "bc01010055"

async def main():
    with open('jtx_commands.json') as f:
        d = json.loads(f.read())
        f.close()
    device = await BleakScanner.find_device_by_address(ADDRESS, timeout=20.0)    
    if not device:
        raise BleakError(f"A device with address {ADDRESS} could not be found.")
    for cmnd in sys.argv[1:] :
        async with BleakClient(device) as client:
            await client.write_gatt_char(CHARACTERISTIC, bytearray.fromhex(d[cmnd]))
        print(f"send {cmnd}")

if __name__ == "__main__":
    asyncio.run(main())