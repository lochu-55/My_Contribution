import micropython

# Print stack usage
print("Stack usage:", micropython.stack_use())


"""
(venv) PS C:\Users\vlab\PycharmProjects\MicroPython_codes\micropython_module> ampy --port COM7 run .\stack_usage.py    
Stack usage: 484
print """