
from selenium import webdriver
import pytesseract
from PIL import Image,ImageEnhance
import time
from selenium.common.exceptions import NoSuchElementException
class find:
    def findq(self):

        driver=webdriver.Chrome()
        driver.get("https://www.toutiao.com/")

        # d=driver.find_elements_by_css_selector('#hotNewsWrap > div.pane-module > ul > li > a > div.news-inner > p')
        #d=driver.find_elements_by_css_selector('#hotNewsWrap > div.pane-module > ul > li:nth-child(1) > a > div.news-inner > p')
        #s=driver.find_element_by_css_selector('hotNewsWrap > div.pane-module > ul > li > a > div.news-inner > p.module-title')
        # file=open('hot.txt','w',encoding='utf-8')
        # for s in d:
        #     print(s.text)
        #     file.write(s.text +'\n')
        # file.close()
        #hotNewsWrap > div.pane-module > ul > li:nth-child(1) > a > div.news-inner > p

        driver.find_element_by_xpath('//*[@id="rightModule"]/div[2]/div/div/a/button').click()
        driver.maximize_window()

        driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div/ul/li[1]').click()
        driver.find_element_by_id("account").send_keys("18640576798")
        driver.find_element_by_id("password").send_keys("Aa123456")
        a= driver.current_window_handle

        time.sleep(10)
        driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div/form/input').click()
        time.sleep(10)
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

            a2 = driver.current_window_handle
            driver.find_element_by_link_text('首页').click()
            driver.close()
            for h1 in han:
                if h1!= a2:
                    driver.switch_to_window(h1)

            time.sleep(3)
            driver.find_element_by_xpath(
                        '/html/body/div/div[2]/div[2]/div[2]/ul/li[4]/div/div[2]/div/div[1]/a').click()


if __name__=="__main__":
    ff=find()
    ff.findq()