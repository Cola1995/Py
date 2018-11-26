import csv
from selenium import webdriver
from publicLogin import Login
import time
my_file='userinfo.csv'
data=csv.reader(open(my_file,'r'))
for user in data:
                driver=webdriver.Chrome()
                driver.get("http://wl.youjian8.com/frontend/web/index.php?r=site%2Flogin")
                Login(driver).login(user[0],user[1])
                time.sleep(3)
                Login(driver).logout()
              
