#test case
#-----------------
#1)open the web browser
#2)open the url
#3)enter username and password
#4)click on the login
#5)capture title of the page
#6)verify the title of the page
#7)close browser


from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
sleep(2)
driver.find_element(By.NAME,"username").clear()
driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")

driver.find_element(By.XPATH,"//button[@type='submit']").click()
sleep(2)

act_title = driver.title
exp_title = "OrangeHRM"
def test_title():
    assert act_title == exp_title

driver.close()



