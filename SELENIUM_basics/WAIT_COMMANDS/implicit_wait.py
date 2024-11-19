from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Attribute:

    def __init__(self):
        self.driver = None

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.google.com")
        self.driver.implicitly_wait(4)
    def teardown(self):
        if self.driver is not None:
            self.driver.quit()
    def search_text(self):
        ip = self.driver.find_element(By.NAME, "q")
        ip.send_keys("Selenium")
        ip.submit()
        self.driver.find_element(By.XPATH,"(//h3[text()='Selenium'])[1]").click()


@pytest.fixture(scope="module")
def attr():
    attr = Attribute()
    attr.setup()
    yield attr
    attr.teardown()


@pytest.mark.impwait_cmd
def test_text(attr):
    attr.search_text()

