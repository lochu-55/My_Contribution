micros = pyb.Timer(2, prescaler=0, period=0xffff)
micros.counter(0)

start_micros = micros.counter()
for i in range(5):
    print(i)
    pyb.wfi()
end_micros = micros.counter()

elapsed_micros = end_micros - start_micros
print("Elapsed time:", elapsed_micros, "microseconds")

