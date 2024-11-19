from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By



class IFRAME:

    def __init__(self):
        self.driver = None

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://demo.automationtesting.in/Frames.html")
        self.driver.implicitly_wait(10)

    def teardown(self):
        if self.driver is not None:
            self.driver.quit()

    def check_switchframe(self):
        self.driver.find_element(By.XPATH,"//a[normalize-space()='Iframe with in an Iframe']").click()
        sleep(3)
        outer = self.driver.find_element(By.XPATH,"//iframe[@src='MultipleFrames.html']")
        self.driver.switch_to.frame(outer)

        inner = self.driver.find_element(By.XPATH, "/html/body/section/div/div/iframe")
        self.driver.switch_to.frame(inner)
        sleep(3)

        self.driver.find_element(By.XPATH,"//input[@type='text']").send_keys("welcome")
        sleep(3)

@pytest.fixture(scope="module")
def frame():
    frame = IFRAME()
    frame.setup()
    yield frame
    frame.teardown()


@pytest.mark.alert
def test_checkalert(frame):
    frame.check_switchframe()
