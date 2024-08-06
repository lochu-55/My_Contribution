import pyb
sw = pyb.Switch()
while True:
    #print(sw.value())
    print(sw())
    pyb.delay(1000)