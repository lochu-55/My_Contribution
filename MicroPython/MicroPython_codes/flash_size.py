import pyb
import stm

# Get the unique MCU ID
mcu_id = pyb.unique_id()

# Access the flash size register (STM32F401 specific)
flash_size_kb = stm.mem16[0x1FFF7A22]

# Print the MCU ID and flash size
print("MCU ID:", mcu_id)
print("Flash Size: {} KB".format(flash_size_kb))

#MCU ID: b'U\x00D\x00\x03P2R720 '
#Flash Size: 512 KB
