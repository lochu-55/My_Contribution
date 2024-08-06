import uasyncio as asyncio


async def waiter(flag):
    print("Waiting for the flag to be set...")
    await flag.wait()
    print("Flag is set. Resuming execution.")

async def main():
    # Create a new ThreadSafeFlag
    flag = asyncio.ThreadSafeFlag()

    # Start the waiter task
    task1 = asyncio.create_task(waiter(flag))

    # Wait for some time
    await asyncio.sleep(2)

    # Set the flag
    print("Setting the flag...")
    flag.set()

    # Wait for the waiter task to finish
    await task1

# Run the main coroutine
asyncio.run(main())
