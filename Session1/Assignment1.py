from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Program Files\Python310\Scripts\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")

driver.find_element(By.NAME, "Email").clear()  # to clear the written data
driver.find_element(By.NAME, "Email").send_keys("admin@yourstore.com")

driver.find_element(By.ID, "Password").clear()  # to clear the written data
driver.find_element(By.ID, "Password").send_keys("admin")

driver.find_element(By.XPATH, "//button[@type='submit']").click()  # xpath
print(driver.title)
act_title = driver.title
exp_title = "Dashboard / nopCommerce administration"
if act_title == exp_title:
    print("Login Pass")
else:
    print("Login Fail")
driver.close()
