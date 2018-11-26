from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://www.cnblogs.com/yoyoketang")
# # 添加 cookie
c1 = {u'domain': u'.cnblogs.com',
u'name': u'.CNBlogsCookie',
u'value': u'xxxx',
u'expiry': 1491887887,
u'path': u'/',
u'httpOnly': True,
u'secure': False}
c2 = {u'domain': u'.cnblogs.com',
u'name': u'.Cnblogs.AspNetCore.Cookies',
u'value': u'xxxx',
u'expiry': 1491887887,
u'path': u'/',
u'httpOnly': True,
u'secure': False}
driver.add_cookie(c1) # 添加 2 个值
driver.add_cookie(c2)
time.sleep(3) # 交流 QQ 群：232607095
# 刷新下页面就见证奇迹了
driver.refresh()