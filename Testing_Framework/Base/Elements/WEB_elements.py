from selenium.webdriver.common.by import By
class Locators:
    URL = "https://practicetestautomation.com/practice-test-login/"
    USER_NAME = (By.ID,"username")
    PASS_WORD = (By.ID,"password")
    LOG_IN = (By.XPATH,"//button[@id='submit']")
    PATH = r"C:\Users\vlab\Desktop\final_Framework\final_Framework\Base\utils\Screenshots\WEB_SS"
    LOG_PATH1=r"C:\Users\vlab\Desktop\final_Framework\final_Framework\Base\utils\Logs\WEB_logs\web.log"


class inputs:
    user = "student"
    pswd = "Paword123"