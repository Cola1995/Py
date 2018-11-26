from selenium import webdriver
import pytesseract
from PIL import Image,ImageEnhance
import time
from selenium.common.exceptions import NoSuchElementException

driver=webdriver.Chrome()
driver.get("https://www.toutiao.com/")

driver.find_element_by_xpath('//*[@id="rightModule"]/div[2]/div/div/a/button').click()

'''验证码识别'''
# imgsrc = driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div/form/div[2]/div/img').get_attribute('src')
# print(imgsrc)
# screenImg = "./screenImg.png"
# driver.get_screenshot_as_file(screenImg)
# # 获取验证码的位置
# location = driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div/form/div[2]/div/img').location
#
# # 获取验证码size
#
# size =driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div/form/div[2]/div/img').size
# left = location['x']
# top = location['y']
# right = location['x'] + size['width']
# bottom = location['y'] + size['height']
# print(left, top, right, bottom)
# img = Image.open(screenImg).crop((left, top, right, bottom))
# img = img.convert('L')  # 转换模式：L | RGB
# img = ImageEnhance.Contrast(img)  # 增强对比度
# img = img.enhance(2.0)  # 增加饱和度
# img.save(screenImg)
# print("验证码保存成功")
# img = Image.open(screenImg)
# code = pytesseract.image_to_string(img)
# print(code)
driver.maximize_window()

driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div/ul/li[1]').click()
driver.find_element_by_id("account").send_keys("18640576798")
driver.find_element_by_id("password").send_keys("Aa123456")
a= driver.current_window_handle

time.sleep(10)
driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div/form/input').click()

time.sleep(10)

#driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[2]/ul/li[3]/div/div[2]/div/div[1]/a').click()
driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[2]/ul/li[4]/div/div[2]/div/div[1]/a').click()


time.sleep(10)
han=driver.window_handles
#print(han)
for h in han:
    if h!=a:
        driver.switch_to_window(h)
#driver.find_element_by_xpath('//ul/li[3]/div/div[2]/div/div[1]/a').click()

js = "window.scrollTo(0,300)"#针对Chrome有效
driver.execute_script(js)

try:
    t=driver.find_element_by_xpath('//*[@id="comment"]/div[2]/div/div[2]/div[2]/div')    #找到评论按钮的位置
#t.click()
#driver.find_element_by_xpath('//*[@id="comment"]/div[2]/div/div[2]/div[1]/textarea').send_keys('ssssss')
except NoSuchElementException as msg:
    print("未找到该元素%s"%msg)

else:
    driver.execute_script("arguments[0].scrollIntoView();", t)#滑动到输入框位置
    #while(1):
    driver.find_element_by_xpath('//*[@id="comment"]/div[2]/div/div[2]/div[1]/textarea').clear()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="comment"]/div[2]/div/div[2]/div[1]/textarea').send_keys("真好")
    time.sleep(3)
    t.click()

    #driver.quit()