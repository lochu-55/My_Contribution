import machine


# Function to perform a time-critical operation
def critical_operation():
    # Disable interrupts and save the current state
    print("disabling the interrupts..")
    irq_state = machine.disable_irq()

    try:
        # Perform a small amount of time-critical work here
        # For example, updating a shared resource safely
        # Note: Keep this section as short as possible
        shared_resource = 42  # Example of critical operation
        shared_resource += 1
        print("Critical operation performed: shared_resource =", shared_resource)

    finally:
        # Re-enable interrupts, restoring the previous state
        print("enabling the interrupts..and restoring the previous state")
        machine.enable_irq(irq_state)


# Main code execution
print("Starting main code execution")

# Perform the critical operation
critical_operation()

print("Main code execution continues")
