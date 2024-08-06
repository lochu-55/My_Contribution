sw = pyb.Switch()
while True:
    sw.callback(lambda:print('pressed!!'))
    pyb.delay(1000)