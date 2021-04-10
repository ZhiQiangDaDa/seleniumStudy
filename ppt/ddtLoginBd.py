import ddt,unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def readData():
    return[['123456','psd','请输入帐号密码'],

    ]
@ddt.ddt 
class testLogin(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
       # self.wait=WebDriverWait.until(self.webdriver.find_element_by_id("TANGRAM__PSP_11__userName"))
        self.wait=WebDriverWait(webdriver,3)
        self.url="https://www.baidu.com/"

    def tearDown(self):
        pass
        #为了查看每次用例的执行结果。我把关闭browse的操作屏蔽了
        # self.driver.quit()
    def find_by_id(self,ob):
        return  self.driver.find_element_by_id(ob)    


    @ddt.data(*readData())
    @ddt.unpack
    def test_moveToLogin(self,name,pwd,text):
       # self.wait=WebDriverWait.until(self.webdriver.find_element_by_id("TANGRAM__PSP_11__userName"))

        self.driver.get(self.url)
        WebDriverWait(webdriver,3)
       # WebDriverWait(self.driver, 10).until(lambda the_driver: the_driver.find_element_by_id('kw'), '失败')
        # sleep(5)
         
        self.driver.find_element(By.ID,"s-top-loginbtn").click()
        #需要等到页面加载出来才能找到下面的元素。此处等待1s，由于网络原因，可能会存在问题，
        #TODO 看使用怎样的等待方法
        #sleep(1)
       #这是错误的写法
        element=WebDriverWait(self.driver, 10).until(lambda the_driver: the_driver.find_element_by_id('TANGRAM__PSP_11__footerULoginBtn'), '失败')
        element.click()
        self.driver.find_element_by_id("TANGRAM__PSP_11__footerULoginBtn").click()
        sleep(1)
        self.name_input=  self.find_by_id('TANGRAM__PSP_11__userName')
        self.psd_input= self.find_by_id("TANGRAM__PSP_11__password")
        self.submit= self.find_by_id("TANGRAM__PSP_11__submit")
        # sleep(1)
        self.name_input.send_keys(name)
        self.psd_input.send_keys(pwd)
        self.submit.click()
        # self.name_input=self.driver.find_element_by_id(TANGRAM__PSP_11__userName)
        # self.psd_input=self.driver.find_element_by_id(TANGRAM__PSP_11__password)
        # self.submit=self.driver.find_element_by_id(TANGRAM__PSP_11__submit)
        # self._name_Login.click
    # def test_into(self):
       



if __name__=='__main__':
    unittest.main()                                                                                                                                                                                                                                                                                                                                                                                                                                                        
