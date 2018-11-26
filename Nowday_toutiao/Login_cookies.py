from selenium import webdriver
import time
import pytesseract
from PIL import Image,ImageEnhance
import time
import json
#
# driver=webdriver.Chrome()
# driver.get("http://hpower.youjiana.com/sso/login/")

# time.sleep(6)
# driver.find_element_by_id("loginform-username").send_keys('13426028026')
# driver.find_element_by_id("loginform-password").send_keys('zxcvbnm*963.')
# driver.find_element_by_name("login-button").click()
# cookies = driver.get_cookies()
# print (type(cookies))
# # print ("".join(cookies))
# f1 = open('cookie.txt', 'w')
# f1.write(json.dumps(cookies))
# f1.close


# driver.find_element_by_id("username").send_keys('guanliyuan')
# driver.find_element_by_id("password").send_keys('youjian@2018')
# time.sleep(10)
# driver.find_element_by_id("login-bt").click()
# cookies = driver.get_cookies()
# print (type(cookies))
# # print ("".join(cookies))
# f1 = open('cookie.txt', 'w')
# f1.write(json.dumps(cookies))
# f1.close

#
# f1 = open('cookie.txt')
# cookie = f1.read()
# cookie =json.loads(cookie)
# for c in cookie:
#     driver.add_cookie(c)
# # # 刷新页面
# driver.refresh()
texi=open('hot.txt','r',encoding='utf-8')
vv=texi.readlines()
for i in vv:
    print(i)