from selenium import webdriver
import unittest,time
from HTMLTestRunner import HTMLTestRunner

class BaiduIde(unittest.TestCase):
                '''百度测试类'''
                def setUp(self):
                                self.driver=webdriver.Chrome()
                                self.driver.implicitly_wait(30)
                                self.base_url="http://www.baidu.com/"
                                self.verificationErrors=[]
                                self.accept_next_alert=True
                                
                def test_baidu_ide(self):
                                '''搜索关键字：selenium ide'''
                                driver=self.driver
                                driver.get(self.base_url+"/")
                                driver.find_element_by_id("kw").send_keys("selenium  ide")
                                driver.find_element_by_id("su").click()
                                try:
                                                self.assertEqual("selenium ide_百度搜索",driver.title)
                                except AssertionError as e:
                                                self.verificationErrors.append(str(e))

                def tearDown(self):
                                self.driver.quit()
                                self.assertEqual([],self.verificationErrors)

if __name__=="__main__":
                #unittest.main()
                suite=unittest.TestSuite()
                suite.addTest(BaiduIde("test_baidu_ide"))
                now_time=time.strftime("%Y_%m_%d_%H_%M_%S")
                fp=open("./report"+now_time+".html","wb")
                runner =HTMLTestRunner(stream=fp,title="百度测试报告",description='用例执行情况')
                runner.run(suite)
                fp.close()
