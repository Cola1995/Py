import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')

driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('su').click()

time.sleep(2)

#方法一:
#将滚动条滚动到页面底部
# js = "documentElement.scrollTop=1000"#针对Firefox有效
js = "window.scrollTo(10,10)"#针对Chrome有效
driver.execute_script(js)

#将滚动条滚动到页面顶部
# js = "documentElement.scrollTop=0"
# driver.execute_script(js)

