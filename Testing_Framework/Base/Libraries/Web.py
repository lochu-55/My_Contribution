from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from Base.Elements.WEB_elements import Locators

options = Options()
options.add_experimental_option("detach", True)
obj = Locators()


class automate_web:

    def __init__(self):
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(obj.URL)
        self.driver.save_screenshot(obj.PATH + r"\excp1.png")

    def close_web(self):
        self.driver.close()

    def enter_username(self, user_input):
        try:
            self.driver.find_element(*obj.USER_NAME).send_keys(user_input)

        except Exception as ex:
            print(ex)

        except NoSuchElementException:
            self.driver.save_screenshot(obj.PATH + r"\username.png")

    def enter_password(self,pswd_input):
        try:
            self.driver.find_element(*obj.PASS_WORD).send_keys(pswd_input)
        except Exception as ex:
            print(ex)
            self.driver.save_screenshot(obj.PATH + r"\excp2.png")
        except NoSuchElementException:
            i = self.driver.save_screenshot(obj.PATH + r"\pswd.png")

    def click_submit(self):
        try:
            self.driver.find_element(*obj.LOG_IN).click()
            if self.driver.title == "Logged In Successfully | Practice Test Automation":
                print("login success")
            else:
                print("fail")
                self.driver.save_screenshot(obj.PATH +r"\invalid_credentials.png")
        except Exception as ex:
            print(ex)
            self.driver.save_screenshot(obj.PATH + r"\excp3.png")
        except NoSuchElementException:
            i = self.driver.save_screenshot(obj.PATH + r"\login.png")


