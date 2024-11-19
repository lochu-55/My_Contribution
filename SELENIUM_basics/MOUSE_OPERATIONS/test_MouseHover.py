from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import pytest
from time import sleep


class MOUSE_OP:

    def __init__(self):
        self.driver = None

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://testsigma.com/automated-api-testing")
        self.driver.implicitly_wait(10)

    def teardown(self):
        if self.driver is not None:
            self.driver.quit()

    def mouse_hover(self):
        Products = self.driver.find_element(By.XPATH,"//p[normalize-space()='Products']")
        Web = self.driver.find_element(By.XPATH,"//a[normalize-space()='Automated Website Testing']")
        act = ActionChains(self.driver)
        sleep(2)
        act.move_to_element(Products).move_to_element(Products).move_to_element(Web).click().perform()
        sleep(3)





@pytest.fixture(scope="module")
def m():
    m = MOUSE_OP()
    m.setup()
    yield m
    m.teardown()


@pytest.mark.mouse_hover
def test_hover(m):
    m.mouse_hover()
