# from selenium import webdriver
# Selenium3
# driver= webdriver.Chrome(executable_path="C:/Program Files/Python310/Scripts/chromedriver.exe")
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# #driver.find_element("autofocus")
# # driver.find_element(name="username").send_keys("Admin")
# act_title=driver.title
# exp_title="OrangeHRM"
# if act_title==exp_title:
#     print("LOgin Test Pass")
# else:
#     print("Login Test Failed")
# driver.close()


# Selenium4

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# serv_obj = Service("C:\Program Files\Python310\Scripts\chromedriver.exe")
# driver = webdriver.Chrome(service=serv_obj)
driver = webdriver.Chrome()    #without url also it will run
driver.implicitly_wait(5)  # session-5  to reload

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

driver.maximize_window()  # to maximise the window
driver.find_element(By.NAME, "username").clear()    #to clear the name space

driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")

driver.find_element(By.XPATH, "//button[@type='submit']").click()  # xpath upcoming videos

print(driver.title)  # orange HRM
act_title = driver.title
exp_title = "OrangeHRM"
if act_title == exp_title:
    print("Login Test Pass")
else:
    print("Login Test Failed")

driver.close() # to close the tab
