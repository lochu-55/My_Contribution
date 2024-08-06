import pyb

def f():
    pyb.LED(1).toggle()

# Initialize Timer 1 with a frequency of 20 Hz
tim1 = pyb.Timer(1, freq = 20)

# Set the callback function for Timer 1

tim1.callback(f)
print(pyb.freq())



