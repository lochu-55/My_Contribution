import pyb
import time
# Initialize an LED to indicate the state
led = pyb.LED(1)

# Function to toggle the LED on interrupt
def handle_interrupt(line):
    print("Interrupt occurred on line:", line)
    led.toggle()

# Configure an external interrupt on pin C13
pin = pyb.Pin('C13', pyb.Pin.IN, pyb.Pin.PULL_DOWN)
extint = pyb.ExtInt(pin, pyb.ExtInt.IRQ_RISING, pyb.Pin.PULL_DOWN, lambda line: handle_interrupt(line))

# Main loop
while True:
    print("Going to sleep (WFI)...")
    pyb.wfi()  # Enter low-power state until an interrupt occurs
    time.sleep(1)



"""
Going to sleep (WFI)...
Going to sleep (WFI)...
Going to sleep (WFI)...
Going to sleep (WFI)...
Going to sleep (WFI)...
Interrupt occurred on line: 13
Going to sleep (WFI)...
Interrupt occurred on line: 13
Going to sleep (WFI)...
Interrupt occurred on line: 13
Going to sleep (WFI)...
Interrupt occurred on line: 13
Interrupt occurred on line: 13
Going to sleep (WFI)...
Interrupt occurred on line: 13
Interrupt occurred on line: 13
Going to sleep (WFI)...
Interrupt occurred on line: 13
Going to sleep (WFI)...
Interrupt occurred on line: 13
"""
