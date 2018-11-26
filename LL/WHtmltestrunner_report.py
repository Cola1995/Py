from HTMLTestRunner import HTMLTestRunner
import time
import unittest
def sen():
    pass


if __name__=="__main__":
    test_dir = r"C:\\Users\\Administrator\\Desktop\\Py\\LL"
    test_report = r"C:\\Users\\Administrator\\Desktop\\Py\\test_report"

    discover = unittest.defaultTestLoader.discover(test_dir,
                                                   pattern='shuju*.py')
    now = time.strftime("%Y-%m-%d_%H-%M-%S")
    filename = test_report + '\\' + now + 'report.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='测试报告',
                            description='用例执行情况：')
    runner.run(discover)
    fp.close()