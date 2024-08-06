from pyb import ADC
import time

# Initialize ADC for internal reference voltage (channel 17)
vref = ADC(17)  # Channel 17 is typically the internal reference voltage

while True:
    # Read the raw ADC value
    raw_value = vref.read()

    # Convert raw_value to voltage using the appropriate formula
    # Assuming VREF+ is 3.3V and ADC is 12-bit (0-4095 range)
    voltage = (raw_value / 4095.0) * 3.3

    # Print the voltage value
    print("VREF Voltage: {:.3f} V".format(voltage))

    # Delay for a short period
    time.sleep(1)

"""
(venv) PS C:\Users\vlab\PycharmProjects\MicroPython_codes> ampy --port COM7 run .\ADC_REFINT.py              
VREF Voltage: 1.203 V
VREF Voltage: 1.202 V
VREF Voltage: 1.202 V
"""