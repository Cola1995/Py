import unittest
from testcase import unittest1

suite=unittest.TestSuite()
suite.addTest(unittest1.TestCount("test_add"))
suite.addTest(unittest1.TestCount("test_add1"))
suite.addTest(unittest1.TestCount("test_sub"))
                 
runner=unittest.TextTestRunner()
runner.run(suite)
