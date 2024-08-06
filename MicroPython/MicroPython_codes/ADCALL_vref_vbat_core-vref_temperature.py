from pyb import ADCAll
import time

# Initialize ADCAll object
adc = ADCAll(12, 0x70000)

# Example function to read and print ADCAll values
def read_adc_values():
    core_vbat = adc.read_core_vbat()
    vref = adc.read_vref()
    core_vref = adc.read_core_vref()
    temp = adc.read_core_temp()

    print("Core VBAT:", core_vbat)
    print("VREF:", vref)
    print("Core VREF:", core_vref)
    print("Internal Temp Sensor:",temp)

# Example usage in a loop
while True:
    read_adc_values()
    time.sleep_ms(1000)  # Delay between readings (1000 milliseconds)

# Optionally, you can deinitialize the ADCAll object when done
adc.deinit()
