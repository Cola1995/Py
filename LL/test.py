from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://hpower.youjiana.com/sso/login")
print(driver.title)
driver.find_element_by_id("username").send_keys("guanliyuan")
driver.find_element_by_id("password").send_keys("youjian@2018")
driver.find_element_by_id("login-bt").click()
time.sleep(3)
driver.close()
