from selenium import webdriver
import sys
import os
path=os.path.abspath(".")
# print(path)
sys.path.append(path+r'\potest\page')
from page.loginpage import LoginPage
import unittest
class LoginCass(unittest.TestCase):
    '''
    第三层
    用例
    '''
    def setUp(self):
        # path=os.path.abspath('.')
        # print(path+r'\potest\page')
        self.url="https://www.baidu.com"
        self.driver=webdriver.Chrome()
    def tearDown(self):
        self.driver.quit()
    def test_serach(self):
       #实例化LoginPage
        login_page=LoginPage(url=self.url,driver=self.driver)
        
        login_page.openLoginPage("要查找的内容")
if __name__=="__main__":
    unittest.main()