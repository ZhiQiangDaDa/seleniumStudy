import unittest
from selenium import webdriver
from time import sleep
from parameterized import parameterized
from selenium.webdriver.support.ui import WebDriverWait
class LoginTest(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver=webdriver.Chrome()
        #搜狐邮箱不能找到相应元素，目前还不知道为什么
        #TODO
        cls.url="https://mail.sohu.com/fe/#/login"
        cls.urls="https:/www.baidu.com"
        cls.urlsr="https://exmail.qq.com/login"
    @classmethod
    def tearDown(cls):
        cls.driver.quit()
    def by_css(self,usernameloc):
        # return self.driver.find_element_by_css_selector(usernameloc)
        # self.driver.switch_to_frame(self.driver.find_element_by_id("SkinClass"))
        # element=self.driver.find_element_by_class_name(usernameloc)
        # self.driver.switch_to_default_content()
        # return element
        return self.driver.find_element_by_id(usernameloc)


    def getassertText(self):
        try:
            return self.by_css('signup_item_content_tips_error').text
        except Exception as message:
            print('元素定位报错，错误原因是:{}'.format(message))
    def sohuLogin(self,user,passwd):
       # self.by_class('input#addFocus ipt-account ng-valid ng-dirty').send_keys("11111")
        # self.driver.find_element_by_class_name("s_ipt").send_keys("11111222.sohu.com")
        # self.driver.find_element_by_css_selector('btn-login fontFamily').click()
        self.by_css("inputuin").send_keys(user)
        self.by_css("pp").send_keys(passwd)
        self.by_css("btlogin").click()

        sleep(3)

    @parameterized.expand([('11111111111','','请输入帐号密码'),('abc222de@sohu.com','','请输入帐号密码'),('','q12314345','请输入帐号密码')])
    # ,('abc222de@sohu.com','','请输入帐号密码'),('','q12314345','请输入帐号密码')
    def test_login(self,username,userpwd,assert_text):
        self.driver.get(self.urlsr)
        WebDriverWait(self.driver, 5).until(lambda the_driver: the_driver.find_element_by_class_name('js_show_pwd_panel'), '未找到该元素').click()
        self.sohuLogin(username,userpwd)
        # self.assertEqual(self.getassertText(),assert_text)
        #TODO
if __name__=="__main__":
    unittest.main(verbosity=2)