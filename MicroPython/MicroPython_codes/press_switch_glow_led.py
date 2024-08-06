sw = pyb.Switch()

#method1
while True:
    sw.callback(lambda:pyb.LED(1).toggle())


#method 2
def led():
    pyb.LED(1).toggle()

while True:
    sw.callback(led)