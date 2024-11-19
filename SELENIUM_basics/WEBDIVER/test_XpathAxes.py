from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class XPATH_AXES:

    def __init__(self):
        self.driver = None

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
        #self.driver.maximize_window()
        sleep(2)

    def teardown(self):
        if self.driver is not None:
            self.driver.quit()

    #absolute path
    def xpath_ax(self):
        #self
        txt = self.driver.find_element(By.XPATH, "//a[contains(text(),'Indian Overseas')]/self::a").text
        print(txt)

        #parent
        txt1= self.driver.find_element(By.XPATH,"//a[contains(text(),'Indian Overseas')]/parent::td").text
        print(txt1)

        #ancestor
        childs = self.driver.find_elements(By.XPATH, "//a[contains(text(),'Indian Overseas')]/ancestor::tr/child::td")
        for i in childs:
            print(i.text)
        sleep(2)

        #descendant
        des = self.driver.find_elements(By.XPATH, "//a[contains(text(),'Indian Overseas')]/ancestor::tr/descendant::*")
        print("no.of descendants : ", len(des))
        print("list of descendants")
        for i in des:
            print(i.text)
        sleep(2)

        # following
        follow = self.driver.find_elements(By.XPATH, "//a[contains(text(),'Indian Overseas')]/ancestor::tr/following::*")
        print("no.of following nodes: ",len(follow))

        # following-sibling
        follow_sib = self.driver.find_elements(By.XPATH,"//a[contains(text(),'Indian Overseas')]/ancestor::tr/following-sibling::*")
        print("no.of following sibling nodes : ",len(follow_sib))

        # following
        pre = self.driver.find_elements(By.XPATH,"//a[contains(text(),'Indian Overseas')]/ancestor::tr/preceding::*")
        print("no.of preceding nodes: ", len(pre))

        # following-sibling
        pre_sib = self.driver.find_elements(By.XPATH,"//a[contains(text(),'Indian Overseas')]/ancestor::tr/preceding-sibling::*")
        print("no.of preceding sibling nodes : ", len(pre_sib))
        return txt



@pytest.fixture(scope="module")
def xpath_axes():
    xpath = XPATH_AXES()
    xpath.setup()
    yield xpath
    xpath.teardown()


@pytest.mark.xpath_axes
def test_absXpath(xpath_axes):
    assert xpath_axes.xpath_ax() == "Indian Overseas"


'''
============================= 1 passed in 46.38s ==============================
PASSED                                  [100%]Indian Overseas
Indian Overseas
Indian Overseas
A
66.76
68.34
+ 2.37
no.of descendants :  7
list of descendants
Indian Overseas
Indian Overseas
A
66.76
68.34
+ 2.37
+ 2.37
no.of following nodes:  2495
no.of following sibling nodes :  288
no.of preceding nodes:  812
no.of preceding sibling nodes :  78
'''