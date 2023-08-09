from mavsdk import System

async def main():
    drone = System()
    await drone.connect()

    # Arm the drone
    #await drone.action.arm()

    # Set the takeoff altitude
    #await drone.action.set_takeoff_altitude(5)  # Change the altitude value as needed

    # Take off
    await drone.action.land()
    #await drone.action.disarm()
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
