import unittest

test_dir="./testcase"
discover=unittest.defaultTestLoader.discover(test_dir,pattern='unit*.py')

runner=unittest.TextTestRunner()
runner.run(discover)
