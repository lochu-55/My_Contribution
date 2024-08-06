tim =pyb.Timer(1)
print(tim)
tim.init(freq=10)
print(tim)
print(tim.source_freq())

#timer counter
print(tim.counter())