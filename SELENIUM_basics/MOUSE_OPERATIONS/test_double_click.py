from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import pytest
from time import sleep


class MOUSE_RIGHT_CLICK:

    def __init__(self):
        self.driver = None

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3")
        self.driver.implicitly_wait(5)

    def teardown(self):
        if self.driver is not None:
            self.driver.quit()

    def double_click(self):
        self.driver.switch_to.frame("iframeResult")
        ip = self.driver.find_element(By.ID,"field1")
        ip.clear()
        ip.send_keys("lochuuu!!")
        btn = self.driver.find_element(By.XPATH,"//button[normalize-space()='Copy Text']")
        act = ActionChains(self.driver)
        sleep(2)
        act.double_click(btn).perform()
        sleep(3)






@pytest.fixture(scope="module")
def m():
    m = MOUSE_RIGHT_CLICK()
    m.setup()
    yield m
    m.teardown()


@pytest.mark.mouse_double
def test_doubleClick(m):
    m.double_click()
