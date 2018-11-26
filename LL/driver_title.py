from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get("http://wl.youjian8.com/frontend/web/index.php?r=site%2Flogin/")
driver.find_element_by_id("loginform-username").send_keys('13426028026')
driver.find_element_by_id("loginform-password").send_keys('zxcvbnm*963.')
driver.find_element_by_name("login-button").click()
time.sleep(3)
print(driver.title)
