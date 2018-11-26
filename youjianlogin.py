from selenium import webdriver
import time
from publicLogin import Login
#driver=webdriver.Chrome()
#driver.get("http://wl.youjian8.com/frontend/web/index.php?r=site%2Flogin")
#Login(driver).login("13426028026","zxcvbnm*963.")
#time.sleep(3)
#Login(driver).logout()

dict={"13426028026":"zxcvbnm*963.","18713658081":"123456"}

for k,v in dict.items():
                driver=webdriver.Chrome()
                driver.get("http://wl.youjian8.com/frontend/web/index.php?r=site%2Flogin")
                Login(driver).login(k,v)
                time.sleep(3)
                Login(driver).logout()
               
 
