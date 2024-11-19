from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class COND:

    def __init__(self):
        self.driver = None

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
        sleep(2)

    def teardown(self):
        if self.driver is not None:
            self.driver.quit()

    # tag id
    def displayed(self):
        search = self.driver.find_element(By.ID,"small-searchterms")
        return search.is_displayed()

    def enabled(self):
        en = self.driver.find_element(By.ID, "small-searchterms")
        return en.is_enabled()

    #s_selected() - for radio buttons and check boxes
    def selected(self):
        male = self.driver.find_element(By.ID, "gender-male")
        female = self.driver.find_element(By.ID, "gender-female")
        print("default status of radio button..")
        print("male status : ",male.is_selected())
        print("female status : ",female.is_selected())
        female.click()
        print("after selecting the female radio button..")
        print("male status : ", male.is_selected())
        print("female status : ", female.is_selected())
        return female.is_selected()

@pytest.fixture(scope="module")
def con():
    con = COND()
    con.setup()
    yield con
    con.teardown()


@pytest.mark.cond_cmd
def test_display(con):
   assert con.displayed() == True


@pytest.mark.cond_cmd
def test_enable(con):
    assert con.enabled() == True

@pytest.mark.cond_cmd
def test_gender(con):
    con.selected() == True
