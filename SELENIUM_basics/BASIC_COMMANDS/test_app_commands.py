from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class APP:

    def __init__(self):
        self.driver = None

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        sleep(2)

    def teardown(self):
        if self.driver is not None:
            self.driver.quit()

    # tag id
    def title_page(self):
        return self.driver.title

    def url_page(self):
        return self.driver.current_url

    def view_page_src(self):
        return self.driver.page_source

@pytest.fixture(scope="module")
def app():
    app = APP()
    app.setup()
    yield app
    app.teardown()


@pytest.mark.app_cmd
def test_title(app):
   assert app.title_page() == "OrangeHRM"


@pytest.mark.app_cmd
def test_url(app):
    assert app.url_page() == "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

@pytest.mark.app_cmd
def test_url(app):
    print(app.view_page_src())
