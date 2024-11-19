from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import yaml

yaml_file_path = "../YAML/login.yaml"
@pytest.fixture
def account_data():
    with open(yaml_file_path, "r") as file:
        data = yaml.safe_load(file)
    return data


class CSS:
    def __init__(self):
        self.driver = None

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.facebook.com/")
        sleep(2)

    def teardown(self):
        if self.driver is not None:
            self.driver.quit()

    def tag_classAttribute(self, username, password):
        clsattr = self.driver.find_element(By.CSS_SELECTOR, "input.inputtext[type=text]")
        clsattr.clear()
        clsattr.send_keys(username)
        sleep(2)
        clspswd = self.driver.find_element(By.CSS_SELECTOR, "input.inputtext[type=password]")
        clspswd.clear()
        clspswd.send_keys(password)
        sleep(2)
        return clsattr.get_attribute('value'), clspswd.get_attribute('value')


@pytest.fixture(scope="module")
def css():
    css = CSS()
    css.setup()
    yield css
    css.teardown()


@pytest.mark.css_selector
def test_attr(css, account_data):
    for account in account_data["accounts"]:
        username, password = account["username"], account["password"]
        returned_username, returned_password = css.tag_classAttribute(username, password)
        assert username == returned_username
        assert password == returned_password
