import pyb

# Initialize ADC for channels PA1 and PA4
adc1 = pyb.ADC(pyb.Pin('PA1'))  # Initialize ADC for PA1 connected to 3.3V pin
adc4 = pyb.ADC(pyb.Pin('PA4'))  # Initialize ADC for PA4 connected to GND pin

def read_adc_values():
    value1 = adc1.read()  # Read value from ADC channel PA1
    value4 = adc4.read()  # Read value from ADC channel PA4
    return value1, value4

def main():
    while True:
        adc_values = read_adc_values()
        print("ADC Channel PA1:", adc_values[0])
        print("ADC Channel PA4:", adc_values[1])
        pyb.delay(1000)  # Wait for 1 second

if __name__ == "__main__":
    main()

"""
(venv) PS C:\Users\vlab\PycharmProjects\MicroPython_codes> ampy --port COM7 run .\ADC_Multi_channel.py       
ADC Channel PA1: 4095
ADC Channel PA4: 3
ADC Channel PA1: 4095
ADC Channel PA4: 2
ADC Channel PA1: 4095
ADC Channel PA4: 4
ADC Channel PA1: 4095
ADC Channel PA4: 2
ADC Channel PA1: 4095
ADC Channel PA4: 2
ADC Channel PA1: 4095
ADC Channel PA4: 2
"""