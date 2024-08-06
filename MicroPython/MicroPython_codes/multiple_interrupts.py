from pyb import Pin, Timer, UART
import time
import machine

# Initialize UART for debugging
uart = UART(2, baudrate=115200)

# Define interrupt flags
button_pressed_flag = False
timer_interrupt_flag = False

# Button press interrupt handler
def button_pressed(pin):
    global button_pressed_flag
    button_pressed_flag = True


# Timer interrupt handler
def timer_interrupt(timer):
    global timer_interrupt_flag
    timer_interrupt_flag = True


# Initialize the button pin as an input with pull-down resistor
button = Pin('PC13', Pin.IN, Pin.PULL_DOWN)

# Attach an interrupt to the button pin
button.irq(trigger=Pin.IRQ_RISING, handler=button_pressed)

# Initialize the timer
try:
    timer = Timer(1, freq=1)  # Set timer to trigger every second
    timer.callback(timer_interrupt)
except ValueError as e:
    uart.write("Timer error: {}\n".format(e))
    raise e

# Main loop
while True:
    # Handle button press first as it has higher priority
    if button_pressed_flag:
        machine.disable_irq()
        button_pressed_flag = False
        uart.write('Button pressed!\n')
        if uart.any():
            print(uart.read())
        machine.enable_irq()

    # Handle timer interrupt next
    if timer_interrupt_flag:
        machine.disable_irq()
        timer_interrupt_flag = False
        uart.write('Timer interrupt!\n')
        if uart.any():
            print(uart.read())
        machine.enable_irq()


    time.sleep(0.1)  # Small delay to debounce and yield processor
