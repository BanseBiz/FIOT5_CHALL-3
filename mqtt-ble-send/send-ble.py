from bleak import BleakClient
from bleak import BleakClient, BleakScanner
from bleak.exc import BleakError

ADDRESS = "ff:21:09:28:22:5a"
CHARACTERISTIC = ""



async def main():
    device = await BleakScanner.find_device_by_address(ADDRESS, timeout=20.0)
    if not device:
        raise BleakError(f"A device with address {ble_address} could not be found.")
    async with BleakClient(device) as client:
        svcs = await client.get_services()
        print("Services:")
        for service in svcs:
            print(service)


if __name__ == "__main__":
    asyncio.run(main())