from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class DROP_DOWN:

    def __init__(self):
        self.driver = None

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://demo.automationtesting.in/Register.html")
        self.driver.implicitly_wait(10)

    def teardown(self):
        if self.driver is not None:
            self.driver.quit()

    # select multiple check boxes at a time
    def select_country(self):
        ele = self.driver.find_element(By.XPATH,"//select[@id='Skills']")
        country = Select(ele)
        country.select_by_visible_text("Configuration")
        sleep(3)
        country.select_by_index(6)
        sleep(3)
        country.select_by_value("APIs")
        sleep(3)
        return ele.get_attribute('value')

    def using_optionxpath(self):
        ele = self.driver.find_element(By.XPATH, "//*[@id='Skills']/option[7]")
        ele.click()
        return ele.get_attribute('value')

    def count_options(self):
        ele = self.driver.find_element(By.XPATH, "//select[@id='Skills']")
        country = Select(ele)
        all_list = country.options
        for i in all_list:
            print(i.text)
        print("total number of options: ", len(all_list))
        return len(all_list)


    #select otion without built in function
    def select_option(self):
        ele = self.driver.find_element(By.XPATH, "//select[@id='Skills']")
        country = Select(ele)
        all_list = country.options
        for i in all_list:
            if i.text == "Email":
                i.click()
        return ele.get_attribute('value')

@pytest.fixture(scope="module")
def drop():
    drop = DROP_DOWN()
    drop.setup()
    yield drop
    drop.teardown()


@pytest.mark.drop_down
def test_checkvalue(drop):
    assert drop.select_country() == "APIs"

@pytest.mark.drop_down
def test_checknoofoptions(drop):
    assert drop.count_options() == 78

@pytest.mark.drop_down
def test_checkselectedoption(drop):
    assert drop.select_option() == "Email"

@pytest.mark.drop_down
def test_xpathcheckoption(drop):
    assert drop.using_optionxpath() == "Art Design"

