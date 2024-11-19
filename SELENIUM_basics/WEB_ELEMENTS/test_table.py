from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from time import sleep

class TABLE:

    def __init__(self):
        self.Numcol = None
        self.Numrow = None
        self.driver = None

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://testautomationpractice.blogspot.com/")
        self.driver.implicitly_wait(10)

    def teardown(self):
        if self.driver is not None:
            self.driver.quit()

    def check_table(self):
        row = self.driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr")
        self.Numrow = len(row)
        sleep(3)
        column = self.driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[1]/th")
        self.Numcol = len(column)
        ele = self.driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[5]/td[1]").text
        return self.Numrow,self.Numcol,ele
        sleep(3)

    def print_tableElements(self):
        print("printing all rows and columns from table.....")
        for i in range(2,self.Numrow+1):
            for c in range(1,self.Numcol+1):
                ele = self.driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(i)+"]/td["+str(c)+"]").text
                print(ele,end='    ')
            print()

    def print_cond_Author(self):
        print("printing all books of Mukesh from table based on the condition.....")
        for j in range(2,self.Numrow+1):
            author = self.driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(j)+"]/td[2]").text
            if author == "Mukesh":
                book = self.driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(j)+"]/td[1]").text
                print(book,"   ",author)
@pytest.fixture(scope="module")
def tb():
    tb = TABLE()
    tb.setup()
    yield tb
    tb.teardown()


@pytest.mark.table
def test_RowCol(tb):
    r,c,e = tb.check_table()
    assert r == 7
    assert c == 4
    assert e == "Master In Selenium"

@pytest.mark.table
def test_print_table(tb):
    tb.print_tableElements()

@pytest.mark.table
def test_print_cond_Author(tb):
    tb.print_cond_Author()
