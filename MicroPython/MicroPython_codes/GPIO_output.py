import machine
import time

# Configure PA5 as an output
led = machine.Pin('PA5', machine.Pin.OUT)

while True:
    led.value(1)  # Turn the LED on
    print("led turned on: ",led.value())
    time.sleep(1)  # Wait for 1 second
    led.value(0)  # Turn the LED off
    print("led turned off: ", led.value())
    time.sleep(1)  # Wait for 1 second
