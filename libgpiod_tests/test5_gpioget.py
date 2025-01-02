import subprocess
import pytest

# Function to detect available GPIO chips
def detect_gpio_chips():
    try:
        # Run gpiodetect command to detect available GPIO chips
        result = subprocess.run(['gpiodetect'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        if result.returncode != 0:
            raise Exception(f"Error running gpiodetect: {result.stderr.decode()}")

        # Parse the output to extract GPIO chip names
        chips = result.stdout.decode().splitlines()
        gpio_chips = []
        for chip in chips:
            if 'gpiochip' in chip:
                # Extract GPIO chip name (e.g., gpiochip0)
                chip_name = chip.split()[0]
                gpio_chips.append(chip_name)

        return gpio_chips

    except subprocess.CalledProcessError as e:
        raise Exception(f"Error detecting GPIO chips: {e}")

# Function to test gpioget
def test_gpio_get():
    try:
        gpio_chips = detect_gpio_chips()
        assert len(gpio_chips) > 0, "No GPIO chips found"
        
        # Use the first detected GPIO chip (you can modify this to test specific chips)
        gpio_chip = gpio_chips[0]
        gpio_pin = 0  # Replace with actual GPIO pin to test
        
        # Run gpioget command to read the GPIO pin value
        result = subprocess.run(['gpioget', gpio_chip, str(gpio_pin)], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        assert result.returncode == 0, f"Error reading GPIO pin {gpio_pin}: {result.stderr.decode()}"
        
        # Get the pin value
        pin_value = result.stdout.decode().strip()
        assert pin_value in ['0', '1'], f"Expected value 0 or 1, got {pin_value}"
        print(f"GPIO pin {gpio_pin} on {gpio_chip} has value: {pin_value}")
    
    except subprocess.CalledProcessError as e:
        pytest.fail(f"Error running gpioget: {e}")  # Indented block for exception handling

