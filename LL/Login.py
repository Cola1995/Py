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



def openBrower():
                webdriver_handle=webdriver.Chrome()
                return webdriver_handle
def openUrl(driver,url):
                driver.get(url)
                driver.maximize_window()

def finElement(driver,arg):
                username=driver.find_element_by_id(arg['u'])
          
                userpass=driver.find_element_by_id(arg['p'])
               
                l=driver.find_element_by_id(arg['l'])
                return username,userpass,l

def senfValues(eletuple,arg):
                listKey=['name','pass']
                i=0
                for key in listKey:
                                
                                eletuple[i].send_keys("")
                                eletuple[i].clear()
                                
                                eletuple[i].send_keys(arg[key])
                                i+=1
                              
                                eletuple[2].click()
                                
def  getCode(driver):
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
                return code
                
                
def login_text(ele_dict):
                driver=openBrower()
                openUrl(driver,ele_dict['url'])
                ele_tuple=finElement(driver,ele_dict)
                senfValues(ele_tuple,ele_dict)                
if __name__=='__main__':
                url="http://hpower.youjiana.com/sso/login/"
                uname="guanliyuan"
                npass="youjian@2018"
                ele_dict={'u':'username','p':'password','l':'login-bt','name':uname,'pass':npass,'url':url}
                account_dict={'name':uname,'pass':npass}
                login_text(ele_dict)

                                                 
                                                 
                                 

               
               
                
             
                
                                

