from time import sleep
from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
sleep(3)
driver.quit()