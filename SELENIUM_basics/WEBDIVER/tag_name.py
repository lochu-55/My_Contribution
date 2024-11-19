from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.automationpractice.pl/index.php")
sleep(2)

sliders = driver.find_elements(By.CLASS_NAME,"homeslider-container")
print(f"no.of sliders in webpage : {len(sliders)}")
# for i in sliders:
#     print(i)

links = driver.find_elements(By.TAG_NAME,"a")
print(f"no.of links in webpage : {len(links)}")
# for i in links:
#     print(i)

driver.close()