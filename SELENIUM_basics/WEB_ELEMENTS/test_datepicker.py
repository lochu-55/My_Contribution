from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from time import sleep


class Date_picker:

    def __init__(self):
        self.driver = None

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://jqueryui.com/datepicker/")
        self.driver.implicitly_wait(10)

    def teardown(self):
        if self.driver is not None:
            self.driver.quit()

    def enter_date(self):
        self.driver.switch_to.frame(0)
        self.driver.find_element(By.XPATH, "//*[@id='datepicker']").send_keys("10/05/2024")
        sleep(3)

    def select_date(self):
        year = "2020"
        month = "October"
        date = "5"

        res = self.driver.find_element(By.XPATH, "//*[@id='datepicker']")
        res.clear()
        res.click()
        sleep(3)

        while True:
            mon = self.driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
            yr = self.driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text
            if mon == month and yr == year:
                break
            else:
                self.driver.find_element(By.XPATH, "//span[normalize-space()='Prev']").click()
        sleep(3)
        dates = self.driver.find_elements(By.XPATH, "//div[@id='ui-datepicker-div']//table/tbody/tr[2]/td/a")
        for ele in dates:
            if ele.text == date:
                ele.click()
                break
        sleep(3)
        return res.get_attribute('value')


@pytest.fixture(scope="module")
def dt():
    dt = Date_picker()
    dt.setup()
    yield dt
    dt.teardown()


@pytest.mark.date
def test_enterDate(dt):
    dt.enter_date()


@pytest.mark.date
def test_selectDate(dt):
    assert dt.select_date() == "10/05/2020"

# @pytest.mark.date
# def test_print_table(tb):
#     tb.print_tableElements()
#
# @pytest.mark.date
# def test_print_cond_Author(tb):
#     tb.print_cond_Author()
