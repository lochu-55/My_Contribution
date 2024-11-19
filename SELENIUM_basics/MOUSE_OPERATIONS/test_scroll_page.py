from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import pytest
from time import sleep


class SCROLL_PAGE:

    def __init__(self):
        self.driver = None

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://en.wikipedia.org/wiki/Gallery_of_sovereign_state_flags")
        self.driver.implicitly_wait(5)

    def teardown(self):
        if self.driver is not None:
            self.driver.quit()



    def scroll_page_down(self):
        # scroll down page by pixel
        self.driver.execute_script("window.scrollBy(0,3000)", "")
        sleep(3)
        val = self.driver.execute_script("return window.pageYOffset;")
        sleep(3)
        print("number of pixels moved down: ", val)

    def scroll_page_till_requiredElement(self):
        flag = self.driver.find_element(By.XPATH,"//img[@alt='India']")
        self.driver.execute_script("arguments[0].scrollIntoView();",flag)
        sleep(3)
        val = self.driver.execute_script("return window.pageYOffset;")
        sleep(3)
        print("number of pixels moved to required element: ",val)

    def scroll_page_end(self):
        #scroll page till end of the page
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)","")
        sleep(3)
        val = self.driver.execute_script("return window.pageYOffset;")
        sleep(3)
        print("number of pixels moved to end of page: ",val)

    def scroll_page_top(self):
        #scroll page till end of the page
        self.driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)","")
        sleep(3)
        val = self.driver.execute_script("return window.pageYOffset;")
        sleep(3)
        print("number of pixels moved to top of the page: ",val)
@pytest.fixture(scope="module")
def s():
    s = SCROLL_PAGE()
    s.setup()
    yield s
    s.teardown()


@pytest.mark.scroll_page
def test_scrollPage(s):
    s.scroll_page_down()
    s.scroll_page_till_requiredElement()
    s.scroll_page_end()
    s.scroll_page_top()

# number of pixels moved down:  2125
# number of pixels moved to required element:  4845
# number of pixels moved to end of page:  12821
# number of pixels moved to top of the page:  0