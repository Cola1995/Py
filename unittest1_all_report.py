import unittest
from HTMLTestRunner import HTMLTestRunner
import time
test_dir="./testcase" #测试用例存放路径

#找到testcase 下所有以unit开头的py套件
discover=unittest.defaultTestLoader.discover(test_dir,pattern='unit*.py')

if __name__=="__main__":
                #unittest.main()
                #suite=unittest.TestSuite()
                #suite.addTest(BaiduIde("test_baidu_ide"))
                
                now_time=time.strftime("%Y_%m_%d_%H_%M_%S")
                #在test_report下生成一个以时间开头的html报告
                fp=open("./test_report/report"+now_time+".html","wb")
                runner =HTMLTestRunner(stream=fp,title="百度测试报告",description='用例执行情况')

                runner.run(discover)
                fp.close()
