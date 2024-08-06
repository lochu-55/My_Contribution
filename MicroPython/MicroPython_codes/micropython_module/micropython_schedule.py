import micropython
import time

def task1(arg):
    print(f"Task 1 executed withh argument: {arg}")

def task2(arg):
    print(f"Task 2 executed with argument: {arg}")

# Schedule task1 to run asynchronously
micropython.schedule(task1,"Hello")

# Schedule task2
micropython.schedule(task2,123)

# Main program loop
while True:
    print("Main program running...")
    time.sleep(1)
