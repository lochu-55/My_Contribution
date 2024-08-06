import uasyncio as asyncio
from machine import Pin  # Assuming Pin is imported correctly for your hardware setup


async def toggle_led(event):
    print("Waiting for the event to be set...")
    await event.wait()
    print("Event is set. Resuming execution.")
    led = Pin('PA5', Pin.OUT)  # Adjust Pin and setup as per your hardware
    try:
        while True:
            if event.is_set():
                led.value(not led.value())  # Toggle LED
                print("LED toggled.")
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        print("Task cancelled and event cleared")
        event.clear()
        print("the event after cleared returns : ",event.is_set())

async def cancel_task(task, delay):
    await asyncio.sleep(delay)
    task.cancel()


async def main():
    # Create a new event
    event = asyncio.Event()

    # Start the LED toggle task
    task2 = asyncio.create_task(toggle_led(event))

    # Start the cancellation task
    asyncio.create_task(cancel_task(task2, 5))  # Cancel after 5 seconds

    # Wait for some time
    await asyncio.sleep(2)

    # Set the event
    print("Setting the event...")
    event.set()

    # Wait for the toggle_led task to finish
    await task2



# Run the main coroutine
asyncio.run(main())
