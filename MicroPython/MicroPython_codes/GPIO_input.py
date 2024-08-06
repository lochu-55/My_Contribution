import machine
import time

# Configure PA1 as an input
button = machine.Pin('PC13', machine.Pin.IN, machine.Pin.PULL_DOWN)  # PULL_UP or PULL_DOWN based on your circuit

while True:
    if button.value() == 0:  # Button pressed (assuming active-low)
        print("Button pressed!")
    time.sleep(0.1)  # Debounce delay
