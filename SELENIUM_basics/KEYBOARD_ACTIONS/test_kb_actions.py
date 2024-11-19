#ctrl+A
#ctrl+C
#tab
#ctrl+V



from selenium import (webdriver)
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
import pytest
from time import sleep


class KEYBOARD_ACTIONS:

    def __init__(self):
        self.driver = None

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://text-compare.com/")
        self.driver.implicitly_wait(5)

    def teardown(self):
        if self.driver is not None:
            self.driver.quit()



    def check_copy(self):
        # scroll down page by pixel
        ip1 = self.driver.find_element(By.ID,"inputText1")
        ip2 = self.driver.find_element(By.ID, "inputText2")
        sleep(3)
        ip1.send_keys("Lochani")
        act = ActionChains(self.driver)
        sleep(2)
        #ip1 --> ctrl+A select the text
        act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
        sleep(2)
        #ip1 --> ctrl+C copy text
        act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
        sleep(2)
        #press tab key to navigate top ip2
        act.send_keys(Keys.TAB).perform()
        sleep(2)
        #ip2 --> ctrl+V paste thetext
        act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
        sleep(3)



@pytest.fixture(scope="module")
def Key():
    Key = KEYBOARD_ACTIONS()
    Key.setup()
    yield Key
    Key.teardown()


@pytest.mark.keyboard
def test_keyboardACTIONS(Key):
    Key.check_copy()
