from pyb import ADC
import time

# Initialize the ADC on the internal temperature sensor channel (typically ADC channel 16)
temp_sensor = ADC(16)

# Function to convert raw ADC value to temperature
def raw_to_temperature(raw_value):
    # STM32 internal temperature sensor calibration values
    V25 = 0.76  # Voltage at 25 degrees Celsius (in Volts)
    Avg_Slope = 2.5  # Average slope (in mV/degree Celsius)
    V_ref = 3.3  # Reference voltage (in Volts)

    # Convert the raw ADC value to a voltage
    voltage = (raw_value / 4095) * V_ref

    # Calculate temperature in Celsius
    temperature = (voltage - V25) / (Avg_Slope / 1000) + 25

    return temperature

# Continuously read and print the temperature
while True:
    raw_value = temp_sensor.read()
    temperature = raw_to_temperature(raw_value)
    print("Temperature: {:.2f}C".format(temperature))
    time.sleep(1)  # Delay for 1 second between readings

"""
(venv) PS C:\Users\vlab\PycharmProjects\MicroPython_codes> ampy --port COM7 run .\ADC_internal_Temp_Sensor.py
Temperature: 24.33C
Temperature: 24.33C
Temperature: 24.00C
Temperature: 23.68C
Temperature: 23.68C
Temperature: 23.68C
Temperature: 24.65C
"""