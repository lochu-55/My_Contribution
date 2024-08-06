from machine import I2C, Pin
import time

# Define the role of the device: 'MASTER' or 'SLAVE'
ROLE = 'MASTER'  # Change to 'MASTER' for the master device

# Common I2C setup
I2C_ID = 1  # Use the correct I2C peripheral ID for your board
FREQ = 100000
SLAVE_ADDRESS = 0x42  # Choose a valid I2C address

# Initialize I2C as master
i2c = I2C(I2C_ID, freq=FREQ)

if ROLE == 'MASTER':
    while True:
        data_to_send = b'Hello, Slave!'  # Data to be sent to the slave
        i2c.writeto(SLAVE_ADDRESS, data_to_send)
        print(f"Sent to slave: {data_to_send}")
        time.sleep(1)  # Wait for 1 second before sending the next message
else:
    print("Invalid role defined. Set ROLE to 'MASTER'.")
