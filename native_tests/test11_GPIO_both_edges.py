import subprocess
import pytest

def set_gpio_direction():
    command = f'echo in | sudo tee /sys/class/gpio/dummy0/direction'
    subprocess.run(command, shell=True, check=True)
    print("GPIO direction set to 'in'")

def set_gpio_interrupt_edge():
    command = f'echo both | sudo tee /sys/class/gpio/dummy0/edge'
    subprocess.run(command, shell=True, check=True)
    print("GPIO interrupt edge set to 'both rising and falling edges'")

def get_gpio_interrupt_edge():
    command = f'cat /sys/class/gpio/dummy0/edge'
    result = subprocess.check_output(command, shell=True).decode().strip()
    return result

def test_gpio_interrupt_edge():
    set_gpio_direction()

    set_gpio_interrupt_edge()

    edge = get_gpio_interrupt_edge()

    assert edge == 'both', f"Expected 'both rising and falling edges', but got {edge}"

if __name__ == "__main__":
    pytest.main()

