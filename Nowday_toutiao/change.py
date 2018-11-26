# coding=utf-8
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(6)

driver.get("https://www.baidu.com")
time.sleep(2)
elem_news = driver.find_element_by_link_text("新闻")
elem_news.click()  # 点击进入到百度新闻
time.sleep(2)
driver.back()  # 从百度新闻后退到百度首页
time.sleep(2)
driver.forward()  # 百度首页前进到百度新闻
time.sleep(2)
