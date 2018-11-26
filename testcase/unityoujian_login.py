from selenium import webdriver
import unittest,time
from HTMLTestRunner import HTMLTestRunner

class BaiduIde(unittest.TestCase):
                '''友件测试类'''
                def setUp(self):
                                self.driver=webdriver.Chrome()
                                self.driver.implicitly_wait(30)
                                self.base_url="http://wl.youjian8.com/frontend/web/index.php?r=site%2Flogin/"
                                self.verificationErrors=[]
                                self.accept_next_alert=True
                                
                def test_baidu_ide(self):
                                '''搜索关键字：selenium ide'''
                                driver=self.driver
                                driver.get(self.base_url)
                                
                                driver.find_element_by_id("loginform-username").send_keys("13426028026")
                                
                                driver.find_element_by_id("loginform-password").send_keys("zxcvbnm*963.")
                                driver.find_element_by_name("login-button").click()
                                time.sleep(3)
                                try:
                                                self.assertEqual("发货单管理",driver.title)
                                                                
                                except AssertionError as e:
                                                print("找不到这个标题")
                                                #self.verificationErrors.append(str(e))
                                                                 
                                                
                                
                                                
                           

                def tearDown(self):
                                self.driver.quit()
                                #self.assertEqual([],self.verificationErrors)
                                

if __name__=="__main__":
                #unittest.main()
                suite=unittest.TestSuite()
                suite.addTest(BaiduIde("test_baidu_ide"))
                now_time=time.strftime("%Y_%m_%d_%H_%M_%S")
                fp=open("./report"+now_time+".html","wb")
                runner =HTMLTestRunner(stream=fp,title="有件测试报告",description='用例执行情况')
                runner.run(suite)
                fp.close()
