import machine
import time

# Initialize UART (use UART2 which is available on the Nucleo-F401RE)
uart = machine.UART(2, baudrate=115200)

# Main loop to send "hello" over UART
while True:
    uart.write('hello\n')  # Send the message "hello"
    time.sleep(1)  # Wait for 1 second
    if uart.any():  # Check if there is any incoming data
        msg = uart.read()  # Read the received data
        print(msg)

