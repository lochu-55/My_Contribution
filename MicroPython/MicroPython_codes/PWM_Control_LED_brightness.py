from pyb import Pin, Timer
import time

# Define the pin connected to the LED (PA5 for STM32F401)
led_pin = Pin('PA5')

# Create a Timer object using pyb module
tim = Timer(2, freq=1000)  # Timer 2, 1 kHz frequency

# Configure the Timer channel for PWM using pyb module
ch = tim.channel(1, Timer.PWM, pin=led_pin)

# Set initial duty cycle to 1% using pyb module
ch.pulse_width_percent(1)

# Function to ramp up and down the PWM duty cycle
def ramp_pwm():
    try:
        for duty_cycle in range(0, 101, 5):  # Ramp up from 0% to 100%
            ch.pulse_width_percent(duty_cycle)
            time.sleep(0.1)

        for duty_cycle in range(100, -1, -5):  # Ramp down from 100% to 0%
            ch.pulse_width_percent(duty_cycle)
            time.sleep(0.1)

    except KeyboardInterrupt:
        pass

# Execute the ramp_pwm function continuously
while True:
    ramp_pwm()

# Cleanup (though it won't be reached in this script)
tim.deinit()
