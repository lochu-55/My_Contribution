from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class XPATH:

    def __init__(self):
        self.driver = None

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.automationpractice.pl/index.php")
        self.driver.maximize_window()
        sleep(2)

    def teardown(self):
        if self.driver is not None:
            self.driver.quit()

    #absolute path
    def absxpath(self):
        search = self.driver.find_element(By.XPATH, "/html/body/div/div[1]/header/div[3]/div/div/div[2]/form/input[4]")
        sleep(2)
        search.clear()
        search.send_keys("shirts")
        sleep(2)
        return search.get_attribute('value')

    #relative path
    def relxpath(self):
        #search = self.driver.find_element(By.XPATH, "//input[@name='search_query']")
        #search = self.driver.find_element(By.XPATH, "// input[ @ name = 'search_query' and @placeholder='Search']")
        #search = self.driver.find_element(By.XPATH, "// input[ @ name = 'search_query' or @id='Search']")
        #search = self.driver.find_element(By.XPATH, "//input[contains(@id,'search')]")
        search = self.driver.find_element(By.XPATH,"//input[starts-with(@name,'search')]")
        sleep(2)
        search.clear()
        search.send_keys("shirts")
        sleep(2)
        return search.get_attribute('value')

    #xpath option - text()
    def xpath_text(self):
        link_text = self.driver.find_element(By.XPATH,"//a[text() = 'Women']")
        link_text.click()
        sleep(2)
        self.driver.back()
        if link_text.is_enabled():
            return True
        else:
            return False

@pytest.fixture(scope="module")
def xpath_fix():
    xpath = XPATH()
    xpath.setup()
    yield xpath
    xpath.teardown()


@pytest.mark.xpath
def test_absXpath(xpath_fix):
    assert xpath_fix.absxpath() == "shirts"


@pytest.mark.xpath
def test_relXpath(xpath_fix):
    assert xpath_fix.relxpath() == "shirts"


@pytest.mark.xpath
def test_xpathText(xpath_fix):
    assert xpath_fix.xpath_text() == True