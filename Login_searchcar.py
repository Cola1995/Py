#coding=utf-8
import pytesseract
from selenium import webdriver
import time
from PIL import Image,ImageEnhance
import re
import requests
from pytesseract import image_to_string
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import smtplib
from email.mime.text import MIMEText


driver = webdriver.Chrome()
driver.maximize_window()   #全屏
driver.get("http://hpower.youjiana.com/sso/login/")
sreach_windows = driver.current_window_handle
#取到验证码地址
imgsrc=driver.find_element_by_id("captcha").get_attribute('src')
print(imgsrc)
screenImg=r"C:\Users\Administrator\Desktop\screenImg.png"
driver.get_screenshot_as_file(screenImg)
#获取验证码的位置
location=driver.find_element_by_id("captcha").location
#获取验证码size
size=driver.find_element_by_id("captcha").size
left=location['x']
top=location['y']
right=location['x']+size['width']
bottom=location['y']+size['height']
print(left,top,right,bottom)
img=Image.open(screenImg).crop((left,top,right,bottom))
img=img.convert('L') 			#转换模式：L | RGB
img=ImageEnhance.Contrast(img)#增强对比度
img=img.enhance(2.0) 			#增加饱和度
img.save(screenImg)
print("验证码保存成功")
img = Image.open(screenImg)
code = pytesseract.image_to_string(img)
print(code)
#code= pytesser.image_file_to_string(screenImg)
#driver.find_element_by_id("captcha").send_keys(code.strip())
print("ok")
#输入账号，密码登录
driver.find_element_by_id("username").send_keys("guanliyuan")
driver.find_element_by_id("password").send_keys("youjian@2018")
driver.find_element_by_id("checkCode").send_keys(code)
#验证码识别错误手动填写
time.sleep(5) 
driver.find_element_by_id("login-bt").click()

#10秒内每隔500毫秒扫描一次页面变化，当出现指定的元素后结束
#wait = WebDriverWait(driver,20)
#wait.until(lambda driver:  driver.find_element_by_xpath('//*[@id="mCSB_1_container"]/ul/li[9]/a'))
#wait.until(lambda driver:  driver.find_element_by_xpath("//*[@id='mCSB_1_container']/ul/li[8]"))
#点击城市管理下城市管理

#driver.find_element_by_xpath("//*[@id='mCSB_1_container']/ul/li[8]").click()
#driver.find_element_by_xpath("//*[@id='mCSB_1_container']/ul/li[8]/ul/li/a").click()

#driver.implicitly_wait(10)
#driver.find_element_by_xpath("//*[@id='toolbar']/a").click()
#点击车辆管理下-->车辆信息
driver.implicitly_wait(10)
driver.find_element_by_xpath('//*[@id="mCSB_1_container"]/ul/li[9]/a').click()
driver.find_element_by_xpath('//*[@id="mCSB_1_container"]/ul/li[9]/ul/li[1]/a').click()
time.sleep(5)
#搜索车牌号辽AWL285
#wait = WebDriverWait(driver,20)
#wait.until(lambda driver:  driver.find_element_by_xpath('//*[@id="carInfoNumber"]'))
#time.sleep(5)
#driver.execute_script("window.stop()")

#print(driver.find_element_by_tag_name("iframe").get_attribute("src"))
driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
#driver.find_element_by_xpath('//*[@id="carInfoNumber"]').send_keys("辽AWL288")
#driver.find_element_by_xpath('//*[@id="collapseOne"]/div/div[4]/button').click()
#print(driver.find_element_by_xpath("//*[@id='table']/tbody/tr/td").get_attribute("colspan"))

#点击查询按钮
search='辽AWL285'
#driver.find_element_by_xpath('//*[@id="collapseOne"]/div/div[4]/button').click()
print("你输入的车牌号%s"%search)
#if search==driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[2]').text:
  #              print("查到车牌号")
#else :
  #              print("未查到")
x=0
clickcount=0
while 1:
               
                                x+=1
                                #print("查询%d次"%(x-2))
                                print(driver.find_element_by_xpath('//*[@id="main"]/div[2]/div[2]/div[4]/div[1]/span[1]').text)
                                res=driver.find_element_by_xpath('//*[@id="main"]/div[2]/div[2]/div[4]/div[1]/span[1]').text[-5]
                                time.sleep(3)
                                driver.find_element_by_xpath('//*[@id="carInfoNumber"]').clear()
                                time.sleep(3)
                                driver.find_element_by_xpath('//*[@id="carInfoNumber"]').send_keys(search)
                                time.sleep(3)
                                driver.find_element_by_xpath('//*[@id="collapseOne"]/div/div[4]/button').click()
                                clickcount+=1
                                if clickcount<=2:
                                                print("页面加载中...........")
                                else:
                                                print("查询%d次"%(x-2))
                                if  int(res)==1:
                                                print("找到该车辆")
                                                msg_from='991571566@qq.com'
                                                passwd='kvmgnchjqnuqbbji'
                                                msg_to='991571566@qq.com'
                                                subject="测试报告"                                                  
                                                content="车辆信息已查到"
                                                msg = MIMEText(content)
                                                msg['Subject']=subject
                                                msg['From']=msg_from
                                                msg['To']=msg_to
                                                try:
                                                    s=smtplib.SMTP_SSL("smtp.qq.com",465)
                                                    s.login(msg_from,passwd)
                                                    s.sendmail(msg_from,msg_to,msg.as_string())
                                                    print("发送成功")
                                                except s.SMTPException.e:
                                                    print("发送失败")
                                                finally:
                                                    s.quit()
                                                break
                                
                                                  
                                else :
                                                print("未查到")
                
                                                 
                                                 
                                                 
                                 

               
               
                
             
                
                                

