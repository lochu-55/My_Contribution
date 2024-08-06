from machine import Pin
import pyb
# create an I/O pin in output mode
p = Pin('A5', Pin.OUT)

# toggle the pin
p.high()
pyb.delay(10)
p.low()