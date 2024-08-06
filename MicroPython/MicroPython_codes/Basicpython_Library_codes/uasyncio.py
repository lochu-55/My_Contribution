import uasyncio

# Task 1: Define a coroutine
async def coroutine_task():
    print("Task 1 is running...")
    await uasyncio.sleep(1)
    print("Task 1 completed")

# Task 2: Define another coroutine
async def another_coroutine_task():
    print("Task 2 is running...")
    await uasyncio.sleep(2)
    print("Task 2 completed")

# Define a function to run the event loop
async def main():
    # Create tasks
    task1 = uasyncio.create_task(coroutine_task())
    task2 = uasyncio.create_task(another_coroutine_task())

    # Run tasks concurrently
    await uasyncio.gather(task1, task2)

# Run the event loop continuously
while True:
    uasyncio.run(main())


# Task 1 is running...
# Task 2 is running...
# Task 1 completed
# Task 2 completed
# Task 1 is running...
# Task 2 is running...
# Task 1 completed
# Task 2 completed
# Task 1 is running...
# Task 2 is running...
# Task 1 completed
# Task 2 completed
# Task 1 is running...
# Task 2 is running...
# Task 1 completed
# Task 2 completed
# Task 1 is running...
# Task 2 is running...
#
# Aborted!
