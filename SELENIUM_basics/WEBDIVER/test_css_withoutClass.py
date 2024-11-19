from selenium.webdriver.common.by import By

import pytest
from selenium import webdriver
from time import sleep
@pytest.fixture(scope="module")
def driver():
    # Create a WebDriver instance (browser) for each test
    driver = webdriver.Chrome()
    yield driver
    # Teardown - close the browser after each test
    driver.quit()


@pytest.mark.css
def test_tagId(driver):
    driver.get("https://www.facebook.com/")
    email_input = driver.find_element(By.CSS_SELECTOR, "input#email")
    email_input.clear()
    email_input.send_keys("lochu5vilehya@gmail.com")
    assert email_input.is_displayed()


@pytest.mark.css
def test_tagClass(driver):
    driver.get("https://www.facebook.com/")
    email_input = driver.find_element(By.CSS_SELECTOR, "input.inputtext")
    email_input.clear()
    email_input.send_keys("lochu5vilehya@gmail.com")
    assert email_input.get_attribute('value') == "lochu5vilehya@gmail.com"



# tag attribute
@pytest.mark.css
def test_attr(driver):
    driver.get("https://www.facebook.com/")
    attr = driver.find_element(By.CSS_SELECTOR, "input[type=text]")
    attr.clear()
    attr.send_keys("lochu5vilehya@gmail.com")
    sleep(2)
    assert attr.get_attribute('value') == "lochu5vilehya@gmail.com"


# tag class attribute
@pytest.mark.css
def test_Class_Attr(driver):
    driver.get("https://www.facebook.com/")
    clsAttr = driver.find_element(By.CSS_SELECTOR, "input.inputtext[type=text]")
    clsAttr.clear()
    clsAttr.send_keys("lochu5vilehya@gmail.com")
    sleep(2)
    clsPswd = driver.find_element(By.CSS_SELECTOR, "input.inputtext[type=password]")
    clsPswd.send_keys("lochu5vilehya")
    sleep(2)
    assert clsAttr.get_attribute('value') == "lochu5vilehya@gmail.com"
    assert clsPswd.get_attribute('value') == "lochu5vilehya"