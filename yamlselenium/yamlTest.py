import yaml
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import os
import time
def readYaml():
    path=os.getcwd()
    filepath=path+r'\yamlselenium\info.yaml'
    info=open(filepath,'r',encoding='utf-8')
    #在yaml5.1 之前  使用yaml.load是不安全的。虽然仍然能够输出，但是会给出警告
    # calling yaml.load() without Loader=... is deprecated as the default Loader is unsafe
    data=yaml.load(info,Loader=yaml.FullLoader)
    info.close()
    return data
print(readYaml())

class TestSearch(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.url="https://www.baidu.com/"
        WebDriverWait(self.driver,3)
    # pass
    def tearDown(self):
        # self.driver.quit()
        pass
    def  eee(self,name):
        self.driver.find_element_by_id("kw").send_keys(name)
        #函数一定要以小写的test开头否则不执行。 
    def testBdSearch(self):
        print(readYaml()['User']['name'])
        self.driver.get(self.url)
        
        self.eee(readYaml()['User']['name'])
        # self.driver.find_element_by_id("kw").send_keys(readYaml())
        # self.driver.find_element_by_id('kw').send_keys(name)
        time.sleep(3)
   
if __name__=="__main__":
    unittest.main()

