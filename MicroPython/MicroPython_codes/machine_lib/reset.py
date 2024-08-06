import machine

# Function to print the reset cause
def print_reset_cause():
    reset_cause = machine.reset_cause()
    print("Reset Cause:", reset_cause)

# Function to perform a soft reset
def perform_soft_reset():
    print("Performing soft reset...")
    machine.soft_reset()

# Function to enter bootloader mode
def enter_bootloader():
    print("Entering bootloader mode...")
    machine.bootloader()

# Print reset cause
print_reset_cause()

# Perform a soft reset
perform_soft_reset()

# Print reset cause after soft reset
print_reset_cause()

# Enter bootloader mode
enter_bootloader()
