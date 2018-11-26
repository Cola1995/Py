from HTMLTestRunner import HTMLTestRunner
import ddt
import unittest
from selenium import webdriver
import time

dict=[{"username":"13426028026","userpass":"zxcvbnm*963."},{"username":"18713658081","userpass":"123456"}]

@ddt.ddt
class yddt(unittest.TestCase):
    '''友件登录测试类'''
    def setUp(self):
        self.d=webdriver.Chrome()
        self.d.get('http://wl.youjian8.com/frontend/web/index.php?r=site%2Flogin')
    def login(self,username,userpass):

        self.d.find_element_by_id("loginform-username").send_keys(username)
        self.d.find_element_by_id("loginform-password").send_keys(userpass)
        self.d.find_element_by_name("login-button").click()
        time.sleep(5)

    def is_loginsuccess(self):

        try:
            self.d.find_element_by_xpath('//*[@id="w3"]/li[2]/form/button').text
            print(self.d.find_element_by_xpath('//*[@id="w3"]/li[2]/form/button').text)
            return True
        except:
            return False

    @ddt.data(*dict)
    def test_login(self,data):
        '''
        友件数据驱动测试

        '''
        print(data['username'])
        self.login(data['username'],data['userpass'])
        result = self.is_loginsuccess()
        self.assertTrue(result)




    def tearDown(self):
        self.d.quit()


if __name__=="_main__":
    unittest.main()


