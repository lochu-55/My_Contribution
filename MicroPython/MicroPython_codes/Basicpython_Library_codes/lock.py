import asyncio

# Define a shared resource
shared_resource = 0

# Define a coroutine to increment the shared resource
async def increment(lock):
    global shared_resource
    print("Trying to acquire the lock to increment...")
    await lock.acquire()
    print("Lock acquired to increment.")
    shared_resource += 1
    await asyncio.sleep(1)  # Simulate some work
    print("Shared resource incremented to:", shared_resource)
    lock.release()
    print("Lock released after increment.")

# Define a coroutine to decrement the shared resource
async def decrement(lock):
    global shared_resource
    print("Trying to acquire the lock to decrement...")
    await lock.acquire()
    print("Lock acquired to decrement.")
    shared_resource -= 1
    await asyncio.sleep(1)  # Simulate some work
    print("Shared resource decremented to:", shared_resource)
    lock.release()
    print("Lock released after decrement.")

async def main():
    # Create a lock
    lock = asyncio.Lock()

    # Run the coroutines concurrently
    await asyncio.gather(
        increment(lock),
        decrement(lock)
    )

# Run the main coroutine
asyncio.run(main())
