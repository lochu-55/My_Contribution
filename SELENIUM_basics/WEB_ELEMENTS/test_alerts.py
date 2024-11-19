from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By



class ALERT:

    def __init__(self):
        self.driver = None

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        self.driver.implicitly_wait(10)

    def teardown(self):
        if self.driver is not None:
            self.driver.quit()

    def check_alert_Ok(self):
        self.driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click()
        sleep(3)
        alert_window = self.driver.switch_to.alert
        print(alert_window.text)
        sleep(3)
        alert_window.send_keys("lochu")
        #alert_window.accept()
        alert_window.dismiss()
        sleep(3)


@pytest.fixture(scope="module")
def alert():
    alert = ALERT()
    alert.setup()
    yield alert
    alert.teardown()


@pytest.mark.alert
def test_checkalert(alert):
    alert.check_alert_Ok()
