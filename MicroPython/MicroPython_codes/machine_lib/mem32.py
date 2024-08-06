import machine

# Write a value to a 32-bit memory address
address = 0x1000
value = 0xABCD1234
machine.mem32[address] = value

# Read the value from the same address
read_value = machine.mem32[address]

print("Value at address {}: {}".format(hex(address), hex(read_value)))
