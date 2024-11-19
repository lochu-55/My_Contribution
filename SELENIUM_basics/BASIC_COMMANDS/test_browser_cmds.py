from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Browser:

    def __init__(self):
        self.driver = webdriver.Chrome()

    def open_url(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        sleep(3)
        tab = self.driver.find_element(By.PARTIAL_LINK_TEXT, "OrangeHRM")
        tab.click()
        sleep(2)
    def close_tab(self):
        self.driver.close()

    def quit_tab(self):
        self.driver.quit()

@pytest.fixture(scope="module")
def browser():
    browser = Browser()
    yield browser




# @pytest.mark.browser_cmd
# def test_closing(browser):
#     browser.open_url()
#     browser.close_tab()


@pytest.mark.browser_cmd
def test_quitting(browser):
    browser.open_url()
    browser.quit_tab()
