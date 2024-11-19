from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import pytest
from time import sleep


class SLIDER:

    def __init__(self):
        self.driver = None

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
        self.driver.implicitly_wait(5)

    def teardown(self):
        if self.driver is not None:
            self.driver.quit()

    def drag_slider(self):
        min_slider = self.driver.find_element(By.XPATH,"//*[@id='slider-range']/span[1]")
        max_slider = self.driver.find_element(By.XPATH,"//*[@id='slider-range']/span[2]")

        print("location of sliders before moving...")
        print(min_slider.location)   #{'x': 59, 'y': 250
        print(max_slider.location)    #{'x': 412, 'y': 250}
        act = ActionChains(self.driver)
        sleep(2)
        act.drag_and_drop_by_offset(min_slider,100,0).perform()
        sleep(3)
        act.drag_and_drop_by_offset(max_slider, -39, 0).perform()

        print("location of sliders before moving...")
        print(min_slider.location)
        print(max_slider.location)





@pytest.fixture(scope="module")
def sl():
    sl = SLIDER()
    sl.setup()
    yield sl
    sl.teardown()


@pytest.mark.slider
def test_slider(sl):
    sl.drag_slider()
