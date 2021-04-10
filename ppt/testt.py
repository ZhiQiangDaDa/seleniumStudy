import ddt
import unittest

Data=[{'name':"lizz"},{"age":"11"}]
@ddt.ddt
class TestData(unittest.TestCase):
    def setUp(self):
        print('start')
    def tearDown(self):
        print("end")
    @ddt.data(*Data)
    def test_DataDriver(self,Data):
        print("DDT数据演示：",Data)

# class TestString (unittest.TestCase):
#     def test1(self):
#         self.assertEqual('foo'.upper(), 'FOO')
Data2=[
    ['admin','psd','d登录成功'],['admin','pd','登录失败'],['','1','登录失败 ']]
@ddt.ddt
class TestState(unittest.TestCase):
    def setUp(self):
        print("start")
    def tearDown(self):
        print("end")
    #不要忘记加修饰头
    @ddt.data(*Data2)
    #对于数据分割需要用到 ddt.unpack
    @ddt.unpack
    def test_State(self,name,pwd,text):
        print("ddt数据驱动",name)
        print("ddt数据驱动",pwd)
        print('ddt数据驱动',text)
if __name__=='__main__':
    unittest.main()                                                                                                                                                                                                                                                                                                                                                                                                                                                        
