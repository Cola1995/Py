from testcase.count  import Count
class TestCount:
                def test_add(self):
                                try:
                                                j=Count(2,4)
                                                add=j.add()
                                                assert(add==9),'结果错误'
                                except AssertionError as msg:
                                                print(msg)
                                else:
                                                print("test pass")
if __name__=='__main__':
                TestCount.test_add()
                
