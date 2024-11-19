from selenium import webdriver
from time import sleep
import pytest
from selenium.webdriver.chrome.options import Options


class HEADLESS:

    def __init__(self):
        self.driver = None

    def setup(self):
        ops = Options()
        ops.add_argument("--headless")
        self.driver = webdriver.Chrome(options=ops)
        self.driver.get("https://demo.nopcommerce.com/")
        self.driver.implicitly_wait(4)
        print(self.driver.title)
        print(self.driver.current_url)

    def teardown(self):
        if self.driver is not None:
            self.driver.quit()

@pytest.mark.headless
def test_headlessMode():
    h = HEADLESS()
    h.setup()
    h.teardown()
