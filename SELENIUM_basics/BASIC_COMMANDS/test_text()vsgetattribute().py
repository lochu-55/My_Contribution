from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Attribute:

    def __init__(self):
        self.driver = None

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://admin-demo.nopcommerce.com/login?returnUrl=%2F")
        sleep(2)

    def teardown(self):
        if self.driver is not None:
            self.driver.quit()
    def input_text(self):
        ip = self.driver.find_element(By.ID, "Email")
        ip.clear()
        ip.send_keys("abc@gmail.com")
        sleep(2)
        print(ip.text)
        return ip.get_attribute('value')

    def login_btn(self):
        btn = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        print("inner text: ",btn.text)
        print("value of attribute: ", btn.get_attribute('value'))
        print("type of attribute: ", btn.get_attribute('type'))
        return btn.text


@pytest.fixture(scope="module")
def attr():
    attr = Attribute()
    attr.setup()
    yield attr
    attr.teardown()


@pytest.mark.text_cmd
def test_text(attr):
    assert attr.input_text() == "abc@gmail.com"

@pytest.mark.text_cmd
def test_getattr(attr):
    assert attr.login_btn() == "LOG IN"