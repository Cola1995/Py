import unittest
from testcase.count import Count
class TestCount(unittest.TestCase):
                def setUp(self):
                                print("start test")
                
                def test_add(self):
                                t=Count(2,4)
                                add=t.add()
                                self.assertEqual(add,6)
                                print("test case1")

                def test_add1(self):
                                t=Count(5,6)
                                add=t.add()
                                self.assertEqual(add,11)
                                print("test case2")
                @unittest.skip("这条不执行")
                def test_sub(self):
                                t=Count(5,1)
                                sub=t.sub()
                                self.assertEqual(sub,4)
                                print("test case3")

                                
                def tearDown(self):
                                print("test end")
if __name__=="__main__":
                unittest.main()


                
                suite=unittest.TestSuite()
                suite.addTest(TestCount("test_add"))
                suite.addTest(TestCount("test_add1"))
                suite.addTest(TestCount("test_sub"))
                 
                runner=unittest.TextTestRunner()
                runner.run(suite)
