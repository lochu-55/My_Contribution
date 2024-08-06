from machine import Pin, I2C
import time

# Define the role of the device
ROLE = 'SLAVE'  # This device will act as a pseudo-slave

# I2C setup
I2C_ID = 1
FREQ = 100000
SLAVE_ADDRESS = 0x42

# Initialize I2C as master for polling (adjust pins as needed)
i2c = I2C(I2C_ID, freq=FREQ)

# Use GPIO for simple data signaling
data_pin = Pin('B9', Pin.IN, Pin.PULL_UP)  # Adjust pin number as needed

if ROLE == 'SLAVE':
    while True:
        if not data_pin.value():  # Check if pin is pulled low (data received)
            # Simulate reading data from master
            data_received = i2c.readfrom(SLAVE_ADDRESS, 16)
            print(f"Received from master: {data_received}")
            time.sleep(0.1)  # Adjust delay as needed
else:
    print("Invalid role defined. Set ROLE to 'SLAVE'.")
