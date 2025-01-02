import subprocess
import pytest

def write_gpio_low():
    command = f'echo 0 | sudo tee /sys/class/gpio/dummy0/value'
    subprocess.run(command, shell=True, check=True)
    print("GPIO pin set to 'low'")

def test_write_gpio_low():

    write_gpio_low()

    command = f'cat /sys/class/gpio/dummy0/value'
    value = subprocess.check_output(command, shell=True).decode().strip()

    assert value == '0'

if __name__ == "__main__":
    pytest.main()

