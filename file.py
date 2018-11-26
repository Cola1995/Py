from selenium import webdriver
import time
from publicLogin import Login
#driver=webdriver.Chrome()
#driver.get("http://wl.youjian8.com/frontend/web/index.php?r=site%2Flogin")
#Login(driver).login("13426028026","zxcvbnm*963.")
#time.sleep(3)
#Login(driver).logout()

use_file=open('userinfo.txt','r')
values=use_file.readlines()
use_file.close()

for i in values:
                username=i.split(',')[0]
                print(username)
                usepass=i.split(',')[1]
                print(usepass)
                driver=webdriver.Chrome()
                driver.get("http://wl.youjian8.com/frontend/web/index.php?r=site%2Flogin")
                Login(driver).login(username,usepass)
                time.sleep(3)
                Login(driver).logout()

