import machine
import time

# Initialize the watchdog timer with a timeout of 5 seconds
wdt = machine.WDT(timeout=5000)

# Function to simulate a task that resets the watchdog timer
def task():
    for i in range(10):
        print(f"Task iteration {i}: feeding the watchdog")
        time.sleep(1)  # Simulate some work
        wdt.feed()  # Reset the watchdog timer to prevent a reset
    print("Simulating a hang by not feeding the watchdog")
    time.sleep(10)  # Simulate a hang, causing the watchdog to trigger a reset

# Indicate that the program has started (helpful to see a reset loop)
print("Program started")

try:
    # Start the task
    task()
except Exception as e:
    print("An exception occurred:", e)
    # The system will reset if the task fails to feed the watchdog timer

"""
(venv) PS C:\Users\vlab\PycharmProjects\MicroPython_codes> ampy --port COM7 run .\Watchdog_Timer.py
Program started
Task iteration 0: feeding the watchdog
Task iteration 1: feeding the watchdog
Task iteration 2: feeding the watchdog
Task iteration 3: feeding the watchdog
Task iteration 4: feeding the watchdog
Task iteration 5: feeding the watchdog
Task iteration 6: feeding the watchdog
Task iteration 7: feeding the watchdog
Task iteration 8: feeding the watchdog
Task iteration 9: feeding the watchdog
Simulating a hang by not feeding the watchdog
MicroPython v1.23.0-preview.379.gcfd5a8ea3 on 2024-05-23; NUCLEO-F401RE with STM32F401xE
Type "help()" for more information.
>>>"""