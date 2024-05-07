from pywinauto.application import Application
from pywinauto.timings import TimeoutError
from time import sleep
from Base.Elements.STM32_elements import STM
from Base.Libraries.logging import logger
from serial import Serial

obj = STM()
log_obj = logger(obj.LOG_PATH2)

class uart_py:

    def __init__(self):
        self.main_c_window = None
        self.app = Application().start(r"C:\ST\STM32CubeIDE_1.14.1\STM32CubeIDE\stm32cubeide.exe")
        sleep(30)
        self.main_window = self.app.window(title="workspace_1.14.1 - STM32CubeIDE")
        log_obj.logger.info("Waiting for STM32CubeIDE to open...")
        self.main_window.wait('ready', timeout=30)
        log_obj.logger.info("STM32CubeIDE opened successfully...")
        img1 = self.main_window.capture_as_image()
        log_obj.logger.info("capturing the screenshot of main window...")
        sspath = obj.PATH + r"\s1.png"
        img1.save(sspath)

    def file_open(self):
        open_window = None
        try:
            self.main_window.menu_select("File->OpenFile...")
            open_window = self.app.OpenFile
        except Exception as e:
            print(e)

        open_window.type_keys(r"C:\Users\vlab\STM32CubeIDE\workspace_1.14.1\Uart_Counter\Core\Src\main.c")
        open_window.Open.click()

        # Wait until the window with title "workspace_1.14.1 - Uart_Counter/Core/Src/main.c - STM32CubeIDE" opens
        log_obj.logger.info("Waiting for main.c file to open...")
        self.main_c_window = self.app.window(title="workspace_1.14.1 - Uart_Counter/Core/Src/main.c - STM32CubeIDE")
        img2 = self.main_c_window.capture_as_image()
        log_obj.logger.info("capturing the screenshot of file opened in the window...")
        img2.save(obj.PATH + r"\s2.png")
        try:
            self.main_c_window.wait('exists', timeout=60)
            log_obj.logger.info("Opened the main.c file of UART successfully...")
            return True
        except TimeoutError:
            log_obj.logger.error("Failed to open the main.c file of UART within the specified timeout...")
            img3 = self.main_window.capture_as_image()
            img3.save(obj.PATH + r"\s3.png")
            return False

    # debugging section
    def debug_mode(self):
        try:
            self.main_c_window.menu_select("Run->Debug")
            log_obj.logger.info("Debugging the code...")
            confirm_window = self.app.ConfirmPerspectiveSwitch
            confirm_window.wait('exists', timeout=60)
            img4 = confirm_window.capture_as_image()
            log_obj.logger.info("capturing the screenshot of debug window...")
            img4.save(obj.PATH + r"\s4.png")
            confirm_window.Switch.click()
            log_obj.logger.info("Switching to Debug mode...")
            log_obj.logger.info("Debug mode switched successfully...")
            return True
        except TimeoutError:
            log_obj.logger.error("Timed out waiting for switch button to disappear...")
            img5 = self.main_window.capture_as_image()
            img5.save(obj.PATH + r"\s5.png")
            return False
        except Exception as ex:
            log_obj.logger.error("Error occurred during debug mode: %s", ex)
            img6 = self.main_window.capture_as_image()
            img6.save(obj.PATH + r"\s6.png")
            return False

    def Resume(self):
        try:
            sleep(20)
            self.main_c_window.menu_select("Run->Resume")
            log_obj.logger.info("Resuming execution...")
            return True
        except Exception as ex:
            log_obj.logger.error("Error occurred while resuming execution: %s", ex)
            return False

    def connect_to_port(self):
        received_data = None
        try:
            # Open serial port
            ser = Serial('COM3', 115200, timeout=1)
            log_obj.logger.info("Serial port opened successfully.")

            i = 0
            while i < 10:
                # Read data from serial port
                received_data = ser.readline().decode().strip()
                print(received_data)
                i += 1
            log_obj.logger.info("Received data: %s", received_data)
            return received_data

        except Exception as e:
            log_obj.logger.error("Error occurred while connecting to port: %s", e)
            print("Error:", e)
            return None
