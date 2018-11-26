import unittest
from count import Count
class TestCount(unittest.TestCase):
                '''减法类'''
                def setUp(self):
                                print("start test")
                
           

                def test_sub(self):
                                t=Count(5,1)
                                sub=t.sub()
                                self.assertEqual(sub,4)
                                print("test case3")

                                
                def tearDown(self):
                                print("test end")
if __name__=="__main__":
                unittest.main()


                
                #suite=unittest.TestSuite()
                
                #suite.addTest(TestCount("test_sub"))
                 
                #runner=unittest.TextTestRunner()
                #runner.run(suite)
