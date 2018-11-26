from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver=webdriver.Chrome()
driver.get("https://www.baidu.com/")
link = driver.find_element_by_link_text("设置")
ActionChains(driver).move_to_element(link).perform()
driver.find_element_by_link_text("搜索设置").click()
time.sleep(5)
driver.find_element_by_link_text("保存设置").click()
alert=driver.switch_to_alert()
print(alert.text)
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
js="var q=document.documentElement.scrollTop=10000"
driver.execute_script(js)
time.sleep(3)
print("ok")
