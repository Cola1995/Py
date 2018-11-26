from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")

# 获得百度搜索窗口句柄
sreach_windows = driver.current_window_handle
# a.lb:nth-child(7)
# html body div#wrapper div#head div.head_wrapper div#u1 a.lb

# a_links = driver.find_element_by_css_selector("a.lb:nth-child(7)")
# print a_links.text

# links = driver.find_elements_by_link_text('登录')
# print links

driver.find_elements_by_link_text('登录').pop().click()
driver.find_element_by_link_text("立即注册").click()

# driver.find_element_by_link_text('登录').click()
# driver.find_element_by_link_text("立即注册").click()

# 获得当前所有打开的窗口的句柄
all_handles = driver.window_handles

# 进入注册窗口
for handle in all_handles:
    if handle != sreach_windows:
        driver.switch_to.window(handle)
        print ('now register window!')
        print (driver.current_window_handle)
        driver.find_element_by_name("userName").send_keys('username')
        driver.find_element_by_name("phone").send_keys('password')
        time.sleep(2)

# 回到搜索窗口
for handle in all_handles:
    if handle == sreach_windows:
        driver.switch_to.window(handle)
        print ('now sreach window')
        print (driver.current_window_handle)
        driver.find_element_by_id("TANGRAM__PSP_4__closeBtn").click()
        driver.find_element_by_id("kw").send_keys("selenium")
        driver.find_element_by_id("su").click()
        print (driver.current_window_handle)
        time.sleep(5)

#driver.quit()

