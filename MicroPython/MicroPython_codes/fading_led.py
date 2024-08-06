import pyb
from time import sleep

# Configure the timer for PWM
tim = pyb.Timer(2, freq=100)  # Set frequency to 1kHz
tchannel = tim.channel(1, pyb.Timer.PWM, pin=pyb.Pin.board.PA5, pulse_width=0)  # PA5 corresponds to the first LED

# Initialize variables for the breathing effect
cur_width = 0
wstep = 500  # Adjust the step size for speed of breathing effect
max_width = 65535  # Maximum value for 16-bit timer
min_width = 0  # Minimum pulse width

while True:
    tchannel.pulse_width(cur_width)
    sleep(0.01)  # Small delay for smooth transition
    cur_width += wstep

    if cur_width > max_width:
        cur_width = max_width
        wstep *= -1  # Reverse direction

    elif cur_width < min_width:
        cur_width = min_width
        wstep *= -1  # Reverse direction
