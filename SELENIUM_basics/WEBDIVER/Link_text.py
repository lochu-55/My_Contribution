from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
original_window = driver.current_window_handle
sleep(2)

# Clicking on the link with exact text "OrangeHRM, Inc"
driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()
sleep(2)

# Switch to the new window
for window_handle in driver.window_handles:
    print(window_handle)
    if window_handle != original_window:
        driver.switch_to.window(window_handle)
        break

# Print the title of the newly opened webpage
print("Title of the webpage:", driver.title)
driver.close()
driver.quit()