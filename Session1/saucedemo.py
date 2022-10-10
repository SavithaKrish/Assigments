import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Program Files\Python310\Scripts\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.saucedemo.com/")
driver.maximize_window()

driver.find_element(By.NAME,"user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.ID,"login-button").click()
print(driver.title)    #swag Labs
time.sleep(3)


driver.close()