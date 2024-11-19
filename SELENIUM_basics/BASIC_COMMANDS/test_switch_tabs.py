from selenium import (webdriver)
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import pytest
from time import sleep


class TABS:

    def __init__(self):
        self.driver = None

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://demo.nopcommerce.com/")
        self.driver.implicitly_wait(5)

    def teardown(self):
        if self.driver is not None:
            self.driver.quit()

    def new_tab(self):
        #opens new tab but do not switch to that tab
        reglink = Keys.CONTROL + Keys.RETURN
        self.driver.find_element(By.LINK_TEXT, "Register").send_keys(reglink)
        sleep(3)

    def open_tab(self):
        self.driver.get("https://www.opencart.com/")
        self.driver.switch_to.new_window('tab')
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
@pytest.fixture(scope="module")
def st():
    st = TABS()
    st.setup()
    yield st
    st.teardown()


@pytest.mark.open_tab
def test_openTabs(st):
    st.new_tab()
    st.open_tab()