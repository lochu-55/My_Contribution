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
        self.driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
        self.driver.implicitly_wait(10)

    def teardown(self):
        if self.driver is not None:
            self.driver.quit()

    def right_click(self):
        btn = self.driver.find_element(By.XPATH,"//span[normalize-space()='right click me']")
        qt = self.driver.find_element(By.XPATH,"//span[normalize-space()='Quit']")
        act = ActionChains(self.driver)
        sleep(2)
        act.context_click(btn).perform()
        sleep(3)
        qt.click()
        sleep(3)





@pytest.fixture(scope="module")
def m():
    m = MOUSE_RIGHT_CLICK()
    m.setup()
    yield m
    m.teardown()


@pytest.mark.mouse_right
def test_rightClick(m):
    m.right_click()
