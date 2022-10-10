import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Program Files\Python310\Scripts\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://practicetestautomation.com/practice-test-login/")
driver.maximize_window()

name = driver.find_element(By.XPATH, "//section[@id='login']/ul/li[2]/b[1]").text
pas = driver.find_element(By.XPATH, "//section[@id='login']/ul/li[2]/b[2]").text

driver.find_element(By.NAME, "username").send_keys(name)
driver.find_element(By.ID, "password").send_keys(pas)
driver.find_element(By.ID, "submit").click()
time.sleep(3)

print(driver.title)  # Logged In Successfully |Practice Test Automation
driver.close()
