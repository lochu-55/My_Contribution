from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class LINK:

    def __init__(self):
        self.driver = None

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
        self.driver.implicitly_wait(4)

    def teardown(self):
        if self.driver is not None:
            self.driver.quit()

    # select multiple check boxes at a time
    def number_of_link(self):
        ip = self.driver.find_elements(By.TAG_NAME, "a")
        for i in ip:
            print(i.text)
        return len(ip)


    #single check box
    def check_link(self):
        try:
            ip = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Books")))
            ip.click()
            return True
        except TimeoutException:
            print("Link not found or clickable within 10 seconds.")
            return False
        except Exception as e:
            print(f"An error occurred: {e}")
            return False





@pytest.fixture(scope="module")
def link():
    link = LINK()
    link.setup()
    yield link
    link.teardown()

@pytest.mark.check_link
def test_checknooflinks(link):
    assert link.number_of_link() == 60

@pytest.mark.check_link
def test_checklink(link):
    assert link.check_link() == True
