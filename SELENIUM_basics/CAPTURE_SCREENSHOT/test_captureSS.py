import os
from selenium import (webdriver)
import pytest
from time import sleep


class CAPTURE_SS:

    def __init__(self):
        self.driver = None

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://demo.nopcommerce.com/")
        self.driver.implicitly_wait(5)

    def teardown(self):
        if self.driver is not None:
            self.driver.quit()



    def capture_ss(self):
        self.driver.save_screenshot(os.getcwd()+r"\homepage.png")
        self.driver.get_screenshot_as_file(os.getcwd()+r"\file.png")
        #self.driver.get_screenshot_as_png() #self.driver.get_screenshot_as_base64() #saves in binary format
        sleep(3)



@pytest.fixture(scope="module")
def ss():
    ss = CAPTURE_SS()
    ss.setup()
    yield ss
    ss.teardown()


@pytest.mark.screenshot
def test_captureSS(ss):
    ss.capture_ss()