import sys
import os
sys.path.append(os.path.abspath('.')+r'\potest\basepage')
from base_page import BasePage
import os
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage(BasePage):
    '''
    第二层
    页面元素分离，每个元素只定位一次

    '''
    namess="kw"
    username222=((By.ID,'kw'))
    def form_username(self):
       
        # return self.find_element1(username222)
        # return self.dr.find_element_by_id(namess)
        return self.find_id(LoginPage.namess)
        # return self.find_element1(username222)


        # return self.driver.find_element1(username222)    

    def openLoginPage(self,username):
        self.dr.get(self.url)
        # WebDriverWait(self.driver,3)
        # self.driver.find_element_by_id("kw").send_keys("32323") 
        self.form_username().send_keys(username)
        sleep(3)

path1=os.path.abspath('.')   # 表示当前所处的文件夹的绝对路径
print(path1)
path2=os.path.abspath('..')  # 表示当前所处的文件夹上一级文件夹的绝对路径
print(path2)
print("``11`1",sys.path)