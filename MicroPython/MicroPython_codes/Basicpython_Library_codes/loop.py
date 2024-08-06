import asyncio

# Define a coroutine that raises an exception
async def buggy_coroutine():
    print("Running buggy coroutine...")
    # This line will raise a ZeroDivisionError
    result = 1 / 0

# Define a coroutine that raises another exception
async def non_integer():
    print("Running non-integer coroutine...")
    # This line will raise a TypeError
    result = 'a' / 1

# Define an exception handler
def exception_handler(loop, context):
    # The context contains the exception and other information
    print("Exception occurred:", context['message'])
    print("Exception type:", type(context['exception']))
    print("Exception:", context['exception'])
    print("Future:", context['future'])
    # Stop the event loop
    loop.stop()

async def main():
    # Get the current event loop
    loop = asyncio.get_event_loop()

    # Set the exception handler
    loop.set_exception_handler(exception_handler)

    # Create tasks for the buggy coroutines
    task1 = loop.create_task(buggy_coroutine())
    task2 = loop.create_task(non_integer())

    try:
        # Run the tasks until they complete
        await asyncio.gather(task1, task2)
    except Exception as e:
        print("Caught exception:", e)

    # Call the default exception handler manually
    loop.call_exception_handler({
        "message": "Manually triggered exception",
        "exception": Exception("Manual exception"),
        "future": None
    })

    # Stop the event loop (if not already stopped)
    loop.stop()

    # Close the event loop
    loop.close()

# Run the main coroutine
asyncio.run(main())
