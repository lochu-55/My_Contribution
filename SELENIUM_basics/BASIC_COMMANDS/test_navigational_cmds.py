from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class NAV:

    def __init__(self):
        self.driver = None

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
        sleep(2)

    def teardown(self):
        if self.driver is not None:
            self.driver.quit()

    # tag id
    def back_page(self):
        self.driver.back()
        sleep(2)
        return self.driver.title

    def forward_page(self):
        self.driver.forward()
        sleep(2)
        return self.driver.title

    def refresh_page(self):
        self.driver.refresh()
@pytest.fixture(scope="module")
def app():
    app = NAV()
    app.setup()
    yield app
    app.teardown()


@pytest.mark.nav_cmd
def test_back(app):
   assert app.back_page() == "OrangeHRM"


@pytest.mark.nav_cmd
def test_forward(app):
    assert app.forward_page() == "nopCommerce demo store. Register"

@pytest.mark.nav_cmd
def test_refresh(app):
    app.refresh_page()
