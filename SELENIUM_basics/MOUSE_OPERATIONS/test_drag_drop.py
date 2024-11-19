from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import pytest
from time import sleep


class MOUSE_DRAG_DROP:

    def __init__(self):
        self.driver = None

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html#google_vignette")
        self.driver.implicitly_wait(5)

    def teardown(self):
        if self.driver is not None:
            self.driver.quit()

    def double_click(self):
        src = self.driver.find_element(By.ID,"box6")
        target = self.driver.find_element(By.ID,"box106")
        act = ActionChains(self.driver)
        sleep(2)
        act.drag_and_drop(src,target).perform()
        sleep(3)






@pytest.fixture(scope="module")
def m():
    m = MOUSE_DRAG_DROP()
    m.setup()
    yield m
    m.teardown()


@pytest.mark.mouse_drag_drop
def test_dragDrop(m):
    m.double_click()
