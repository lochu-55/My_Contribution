from pyb import Pin, Timer

# Define the pin connected to the LED
led_pin = Pin('PA5')  # Change this to the appropriate pin for your setup

# Create a Timer object
tim = Timer(2, freq=1000)  # Timer 2, with a frequency of 1000 Hz

# Configure the Timer channel for PWM
ch = tim.channel(1, Timer.PWM, pin=led_pin)

# Set the duty cycle to achieve 50% brightness (50% duty cycle)
ch.pulse_width_percent(1)


