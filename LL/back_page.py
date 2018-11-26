from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get('https://www.toutiao.com/')
# driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[2]/ul/li[1]/div/div[2]/div/div[1]/a').click()
# time.sleep(5)
# driver.back()
# print("首页")
driver.get('http://www.runoob.com/python3/python3-set.html')
driver.get('http://124.95.129.86:9000/sso/login')
driver.back()