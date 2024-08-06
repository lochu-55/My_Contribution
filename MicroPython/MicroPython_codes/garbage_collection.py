import gc

# Force a garbage collection
gc.collect()

# Display free memory
print("Free memory:", gc.mem_free()) #Return the free heap size in bytes

#Free memory: 59888
