from selenium import webdriver
import pytest
from time import sleep


class WINDOWS:

    def __init__(self):
        self.driver = None

    def setup(self):
        self.driver = webdriver.Chrome()

    def teardown(self):
        if self.driver is not None:
            self.driver.quit()

    def switch_windows(self):
        self.driver.get("https://www.opencart.com/")
        self.driver.switch_to.new_window('window')
        sleep(2)
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        sleep(2)
@pytest.fixture(scope="module")
def w():
    w = WINDOWS()
    w.setup()
    yield w
    w.teardown()


@pytest.mark.open_window
def test_switchWindows(w):
    w.switch_windows()
