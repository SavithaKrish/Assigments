from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj = Service("C:\Program Files\Python310\Scripts\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.implicitly_wait(5)

driver.get("https://practice.automationtesting.in/my-account/")
driver.maximize_window()

# driver.find_element(By.NAME,"email").send_keys("savikrish25@gmail.com")
# driver.find_element(By.ID,"reg_password").send_keys("Savithak@25")
# driver.find_element(By.NAME,"register").click()

driver.find_element(By.NAME,"username").send_keys("savikrish25@gmail.com")
driver.find_element(By.ID,"password").send_keys("Savithak@25")
driver.find_element(By.NAME,"login").click()

time.sleep(3)

print(driver.title)  #My Account – Automation Practice Site

driver.close()

