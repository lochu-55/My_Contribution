import machine
import time
# Define a function to be called when the interrupt occurs
def button_pressed(b):
    print("Button ",b," pressed!")

# Initialize the button pin as an input with pull-down resistor
button = machine.Pin('PC13', machine.Pin.IN, machine.Pin.PULL_DOWN)
uart = machine.UART(2, baudrate=115200)

# Attach an interrupt to the button pin
button.irq(trigger=machine.Pin.IRQ_RISING, handler=button_pressed)

# Main loop
while True:
    uart.write('hello\n')  # Send the message "hello"
    time.sleep(1)  # Wait for 1 second
    if uart.any():  # Check if there is any incoming data
        msg = uart.read()  # Read the received data
        print(msg)
