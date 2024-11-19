import time
import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Attribute:

    def __init__(self):
        self.driver = None

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.google.com")
        self.mywait=WebDriverWait(self.driver,5,poll_frequency=2,ignored_exceptions=[NoSuchElementException,
                                                                    ElementNotVisibleException,
                                                                    ElementNotSelectableException,
                                                                    Exception]
                                  )

    def teardown(self):
        if self.driver is not None:
            self.driver.quit()
    def search_text(self):
        ip = self.driver.find_element(By.NAME, "q")
        ip.send_keys("Selenium")
        ip.submit()
        search_link = self.mywait.until(EC.presence_of_element_located((By.XPATH, "(//h3[text()='Selenium'])[1]")))
        search_link.click()


@pytest.fixture(scope="module")
def attr():
    attr = Attribute()
    attr.setup()
    yield attr
    attr.teardown()


@pytest.mark.expwait_cmd
def test_text(attr):
    attr.search_text()