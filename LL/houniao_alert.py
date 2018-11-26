from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get("http://hpower.youjiana.com/sso/login/")

#driver.find_element_by_id("username").send_keys("username")
#driver.find_element_by_id("password").send_keys("usepass")

driver.find_element_by_id("login-bt").click()
time.sleep(3)
#ala=driver.switch_to_alert()


#driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div[4]/button').click()
t=driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div[3]')
#t=driver.find_element_by_xpath('//*[@id="jconfirm-box57346"]')
print(t.text)
