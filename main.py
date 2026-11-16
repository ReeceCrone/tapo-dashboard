
import asyncio
from getpass import getpass
from kasa import Discover


async def main():
    ip = "172.16.1.215"

    print(f"Connecting to Tapo device at {ip}...")

    email = input("TP-Link account email: ")
    password = getpass("TP-Link account password: ")

    try:
        device = await Discover.discover_single(
            ip,
            username=email,
            password=password
        )

        if device is None:
            print("Could not identify a device at this IP.")
            return

        await device.update()

        print("\nSuccessfully connected!")
        print("--------------------------")
        print("Device:", device.alias)
        print("Model:", device.model)
        print("IP:", ip)
        print("Powered on:", device.is_on)
        print("--------------------------")
        await device.disconnect()

    except Exception as error:
        print("\nConnection failed!")
        print("Error:", error)


if __name__ == "__main__":
    asyncio.run(main())