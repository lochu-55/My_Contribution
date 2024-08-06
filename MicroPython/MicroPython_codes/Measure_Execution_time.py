import time

start = time.ticks_ms()  # Get current time in milliseconds

# Code block to measure
for i in range(1000000):
    pass

end = time.ticks_ms()  # Get current time in milliseconds
execution_time = time.ticks_diff(end, start)  # Calculate difference
print("Execution Time: {} ms".format(execution_time))


#Execution Time: 5814 ms
