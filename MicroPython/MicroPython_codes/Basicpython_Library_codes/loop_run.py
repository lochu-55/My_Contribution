import asyncio

# Define a coroutine that runs indefinitely
async def infinite_task():
    while True:
        print("Infinite task is running...")
        await asyncio.sleep(1)

# Define a coroutine that completes after a delay
async def finite_task():
    print("Finite task is starting...")
    await asyncio.sleep(3)
    print("Finite task is completed.")

async def stop_loop_after(loop, delay):
    await asyncio.sleep(delay)
    print(f"Stopping loop after {delay} seconds")
    loop.stop()

# Main function to demonstrate the two methods
def main():
    loop = asyncio.get_event_loop()

    # Create the infinite task
    loop.create_task(infinite_task())

    # Create the finite task and run until complete
    loop.run_until_complete(finite_task())

    # Schedule the event loop to stop after 5 seconds
    loop.create_task(stop_loop_after(loop, 5))

    # Run the event loop forever
    print("Running the event loop forever...")
    try:
        loop.run_forever()
    finally:
        print("Closing the event loop.")
        loop.close()

# Run the main function
main()
