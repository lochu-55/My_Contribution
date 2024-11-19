from selenium import webdriver
import pytest
from time import sleep


class COOKIES:

    def __init__(self):
        self.driver = None

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://demo.nopcommerce.com/")
        self.driver.implicitly_wait(4)

    def teardown(self):
        if self.driver is not None:
            self.driver.quit()

    def get_cookies(self):
        cookies = self.driver.get_cookies()
        sleep(2)

        for c in cookies:
            print(c)

        #retrieve the name:value of the cookies
        print("names of the cookies...")
        for c in cookies:
            print(c.get('name'),":",c.get('value'))

        return len(cookies)


    def add_cookie(self):
        self.driver.add_cookie({"name":"MyCookie","value":"123456"})
        cookies = self.driver.get_cookies()
        return len(cookies)

    def del_cookie(self):
        self.driver.delete_cookie("MyCookie")
        cookies = self.driver.get_cookies()
        return len(cookies)

    def del_all_cookies(self):
        self.driver.delete_all_cookies()
        cookies = self.driver.get_cookies()
        return len(cookies)
@pytest.fixture(scope="module")
def c():
    c = COOKIES()
    c.setup()
    yield c
    c.teardown()


@pytest.mark.cookies
def test_cookiesNum(c):
    print(c.get_cookies())

@pytest.mark.cookies
def test_addCookie(c):
    print(c.add_cookie())

@pytest.mark.cookies
def test_delCookie(c):
    print(c.del_cookie())

@pytest.mark.cookies
def test_delallCookie(c):
    print(c.del_all_cookies())
