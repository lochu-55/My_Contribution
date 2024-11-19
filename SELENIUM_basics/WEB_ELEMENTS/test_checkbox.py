from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests as rq

class CHECK:

    def __init__(self):
        self.driver = None

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://testautomationpractice.blogspot.com/")
        self.driver.implicitly_wait(4)

    def teardown(self):
        if self.driver is not None:
            self.driver.quit()

    #single check box
    def check_box(self):
        ip = self.driver.find_element(By.ID, "sunday")
        ip.click()
        sleep(3)
        return ip.is_selected()

    def clear_check(self):
        ch = self.driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id,'day')]")
        for i in ch:
            if i.is_selected():
                i.click()
        sleep(3)
        return ch

    #select multiple check boxes at a time
    def multiple_check(self):
        ch = self.clear_check()
        for i in ch:
            i.click()
        sleep(3)
        return len(ch)

    def cond_check(self):
        ch = self.clear_check()
        for i in ch:
            weekname = i.get_attribute('id')
            if weekname == 'monday' or weekname == 'sunday':
                i.click()
        sleep(3)

        #select last 2 checkboxes
        #range(5,7) ----> 6,7
        #totalnumberofelements-2 = starting index
    def last_two(self):
        ch = self.clear_check()
        for i in range(len(ch)-2,len(ch)):
                ch[i].click()
        sleep(3)

    def first_two(self):
        ch = self.clear_check()
        for i in range(len(ch)):
            if i < 2:
                ch[i].click()
        sleep(3)
@pytest.fixture(scope="module")
def check():
    check = CHECK()
    check.setup()
    yield check
    check.teardown()


@pytest.mark.check_box
def test_checkselect(check):
    assert check.check_box() == True

@pytest.mark.check_box
def test_checkmultiSelect(check):
    assert check.multiple_check() == 7

@pytest.mark.check_box
def test_checkCondSelect(check):
    check.cond_check()

@pytest.mark.check_box
def test_last2select(check):
    check.last_two()

@pytest.mark.check_box
def test_first2select(check):
    check.first_two()