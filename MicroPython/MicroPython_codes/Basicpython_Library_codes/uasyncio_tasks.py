from Basicpython_Library_codes import uasyncio


# Task 1: Fetch data
async def fetch_data(task):
    while True:
        print(f"current task :{task}")
        print("task1 is running..")
        await uasyncio.sleep(2)


# Task 2: Print numbers
async def print_numbers(task):
    i = 0
    while True:
        print(f"current task :{task}")
        print("task2 is running..")
        print(f"Number: {i}")
        i += 1
        await uasyncio.sleep(2)


# Task 3: Toggle an LED
async def toggle_led(task):
    # Replace this with actual code to toggle LED on a regular Python environment
    from machine import Pin
    led = Pin('PA5', Pin.OUT)
    while True:
        print(f"current task :{task}")
        print("task3 is running...")
        led.value(not led.value())
        print("Task toggle_led toggled LED")
        await uasyncio.sleep(2)




async def main():
    # Create and start tasks
    task1 = uasyncio.create_task(fetch_data(uasyncio.current_task()))
    task2 = uasyncio.create_task(print_numbers(uasyncio.current_task()))
    task3 = uasyncio.create_task(toggle_led(uasyncio.current_task()))

    # Wait for some time
    await uasyncio.sleep(5)

    # Cancel task2
    task1.cancel()
    print("task1 is cancelled")

    # Run tasks indefinitely
    await uasyncio.gather(task1, task2, task3, return_exceptions=True)  # Use return_exceptions to suppress cancellation exceptions



# Run the main coroutine
uasyncio.run(main())
