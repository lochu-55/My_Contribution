from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class CSS:

    def __init__(self):
        self.driver = None

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.facebook.com/")
        sleep(2)

    def teardown(self):
        if self.driver is not None:
            self.driver.quit()

    # tag id
    def tag_id(self):
        self.driver.find_element(By.CSS_SELECTOR, "input#email").clear()
        tab = self.driver.find_element(By.CSS_SELECTOR, "input#email")
        tab.send_keys("lochu5vilehya@gmail.com")
        return tab.get_attribute('value')

    def tag_class(self):
        clss = self.driver.find_element(By.CSS_SELECTOR, "input.inputtext")
        clss.clear()
        clss.send_keys("lochu5vilehya@gmail.com")
        return clss.get_attribute('value')

    def tag_attribute(self):
        attr = self.driver.find_element(By.CSS_SELECTOR, "input[type=text]")
        attr.clear()
        attr.send_keys("lochu5vilehya@gmail.com")
        sleep(2)
        return attr.get_attribute('value')

    def tag_classAttribute(self):
        clsattr = self.driver.find_element(By.CSS_SELECTOR, "input.inputtext[type=text]")
        clsattr.clear()
        clsattr.send_keys("lochu5vilehya@gmail.com")
        sleep(2)
        clspswd = self.driver.find_element(By.CSS_SELECTOR, "input.inputtext[type=password]")
        clspswd.send_keys("lochu5vilehya")
        sleep(2)
        return clsattr.get_attribute('value'),clspswd.get_attribute('value')


@pytest.fixture(scope="module")
def css():
    css = CSS()
    css.setup()
    yield css
    css.teardown()


#tag_id
@pytest.mark.css_selector
def test_tagId(css):
    assert css.tag_id() == "lochu5vilehya@gmail.com"


# tag class
@pytest.mark.css_selector
def test_tagclass(css):
    assert css.tag_class() == "lochu5vilehya@gmail.com"

# tag attribute
@pytest.mark.css_selector
def test_attr(css):
    assert css.tag_attribute() == "lochu5vilehya@gmail.com"


# tag class attribute
@pytest.mark.css_selector
def test_clsattr(css):
    val1,val2 = css.tag_classAttribute()
    assert val1 == "lochu5vilehya@gmail.com"
    assert val2 == "lochu5vilehya"



