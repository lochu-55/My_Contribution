from time import sleep
import pytest
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By


class BROKEN_LINK:

    def __init__(self):
        self.driver = None

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.deadlinkcity.com/")
        self.driver.implicitly_wait(4)

    def teardown(self):
        if self.driver is not None:
            self.driver.quit()

    # select multiple check boxes at a time
    def number_of_link(self):
        res = None
        ip = self.driver.find_elements(By.TAG_NAME, "a")
        count = 0
        for i in ip:
            url = i.get_attribute('href')
            try:
                res = requests.head(url)
            except:
                None

            if res.status_code >= 400:
                print(url, "...this is broken link")
                count += 1
            else:
                print(url, "..it is valid link")
        return count




@pytest.fixture(scope="module")
def link():
    link = BROKEN_LINK()
    link.setup()
    yield link
    link.teardown()


@pytest.mark.broken_link
def test_checknoofbrokenlinks(link):
    assert link.number_of_link() == 40



# ============================= test session starts =============================
# collecting ... collected 1 item
#
# test_brokenLinks.py::test_checknoofbrokenlinks
#
# ============================= 1 passed in 39.76s ==============================
# PASSED                    [100%]http://www.deadlinkcity.com/comparison.asp ..it is valid link
# http://www.deadlinkcity.com/errorlist.asp ..it is valid link
# http://www.deadlinkcity.com/error-page.asp?e=400 ...this is broken link
# http://www.deadlinkcity.com/error-page.asp?e=401 ...this is broken link
# http://www.deadlinkcity.com/error-page.asp?e=402 ...this is broken link
# http://www.deadlinkcity.com/error-page.asp?e=403 ...this is broken link
# http://www.deadlinkcity.com/error-page.asp?e=404 ...this is broken link
# http://www.deadlinkcity.com/error-page.asp?e=405 ...this is broken link
# http://www.deadlinkcity.com/error-page.asp?e=406 ...this is broken link
# http://www.deadlinkcity.com/error-page.asp?e=407 ...this is broken link
# http://www.deadlinkcity.com/error-page.asp?e=408 ...this is broken link
# http://www.deadlinkcity.com/error-page.asp?e=409 ...this is broken link
# http://www.deadlinkcity.com/error-page.asp?e=410 ...this is broken link
# http://www.deadlinkcity.com/error-page.asp?e=411 ...this is broken link
# http://www.deadlinkcity.com/error-page.asp?e=412 ...this is broken link
# http://www.deadlinkcity.com/error-page.asp?e=413 ...this is broken link
# http://www.deadlinkcity.com/error-page.asp?e=414 ...this is broken link
# http://www.deadlinkcity.com/error-page.asp?e=415 ...this is broken link
# http://www.deadlinkcity.com/error-page.asp?e=416 ...this is broken link
# http://www.deadlinkcity.com/error-page.asp?e=417 ...this is broken link
# http://www.deadlinkcity.com/error-page.asp?e=420 ...this is broken link
# http://www.deadlinkcity.com/error-page.asp?e=422 ...this is broken link
# http://www.deadlinkcity.com/error-page.asp?e=423 ...this is broken link
# http://www.deadlinkcity.com/error-page.asp?e=424 ...this is broken link
# http://www.deadlinkcity.com/error-page.asp?e=429 ...this is broken link
# http://www.deadlinkcity.com/error-page.asp?e=431 ...this is broken link
# http://www.deadlinkcity.com/error-page.asp?e=450 ...this is broken link
# http://www.deadlinkcity.com/error-page.asp?e=500 ...this is broken link
# http://www.deadlinkcity.com/error-page.asp?e=501 ...this is broken link
# http://www.deadlinkcity.com/error-page.asp?e=502 ...this is broken link
# http://www.deadlinkcity.com/error-page.asp?e=503 ...this is broken link
# http://www.deadlinkcity.com/error-page.asp?e=504 ...this is broken link
# http://www.deadlinkcity.com/error-page.asp?e=505 ...this is broken link
# http://www.deadlinkcity.com/error-page.asp?e=506 ...this is broken link
# http://www.deadlinkcity.com/error-page.asp?e=507 ...this is broken link
# http://www.deadlinkcity.com/error-page.asp?e=509 ...this is broken link
# http://www.deadlinkcity.com/error-page.asp?e=510 ...this is broken link
# http://www.deadlinkcity.com/page-not-found.asp ...this is broken link
# http://www.domaindoesnot.exist/ ...this is broken link
# http://www.deadlinkcity.com/default.asp?r=1 ..it is valid link
# http://www.deadlinkcity.com/default.asp?r=2 ..it is valid link
# http://www.deadlinkcity.com/default.asp?r=4 ..it is valid link
# http://www.deadlinkcity.com/default.asp?r=5 ..it is valid link
# http://www.deadlinkcity.com/default.asp?r=6 ..it is valid link
# http://www.deadlinkcity.com/default.asp?r=7 ..it is valid link
# http://www.deadlinkcity.com/disallowed/disallowed.html ...this is broken link
# http://www.deadlinkcity.com/disallowed/nonexistent.html ...this is broken link
# mailto:info@deadlinkchecker.com?subject=DeadLinkCity.com%20-%20feedback ...this is broken link
#
# Process finished with exit code 0
