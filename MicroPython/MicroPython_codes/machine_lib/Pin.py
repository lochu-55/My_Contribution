import machine

# Initialize a pin as an output pin with an initial value of 0
led_pin = machine.Pin('PA5', machine.Pin.OUT)

# Initialize a pin as an input pin with a pull-up resistor
button_pin = machine.Pin('PC13', mode=machine.Pin.IN, pull=machine.Pin.PULL_UP)



# Function to demonstrate reading and writing pin values
def pin_operations():
    # Set the LED pin high
    led_pin.value(1)
    print("LED pin value set to: " ,led_pin.value())

    # Set the LED pin low using the on/off methods
    led_pin.off()
    print("LED pin value set to: ",led_pin.value())
    led_pin.on()
    print("LED pin value set to: " ,led_pin.value())

    # Read the button pin value
    button_value = button_pin.value()
    print("Button pin value is: " ,button_value)




# Function to demonstrate disabling and enabling interrupts
def critical_section():
    # Disable interrupts
    irq_state = machine.disable_irq()

    try:
        # Perform time-critical operations here
        print("Performing time-critical operations")
        # Example: Toggle the LED pin
        led_pin.value(not led_pin.value())
    finally:
        # Re-enable interrupts
        machine.enable_irq(irq_state)


# Main code execution
print("Starting main code execution")

# Perform pin operations
pin_operations()

#Execute a critical section with interrupts disabled
critical_section()

print("Main code execution continues")
