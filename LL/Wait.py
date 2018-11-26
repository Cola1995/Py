from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("http://hpower.youjiana.com/sso/login")
#print(driver.title)
driver.find_element_by_id("username").send_keys("guanliyuan")
driver.find_element_by_id("password").send_keys("youjian@2018")
#WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,'login-bt'))).click()
#print("ok")
time.sleep(5)
driver.find_element_by_id("login-bt").click()
#time.sleep(3)
#driver.close()
