from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class BasePage(object):
    '''
    第一层，对selenium二次封装，定一个所有页面都继承的basepage
    封装selenium基本方法
    '''


    def __init__(self,url,driver):
        self.url=url
        self.dr=driver
    def find_element1(self,*loc):
        try:
            WebDriverWait(self.dr,10).until(EC.visibility_of_element_located(loc))
            return self.find_element1(*loc)
        except:
            print(*loc+'元素无法在页面中找到')
    def find_id(self,loc):
        return self.dr.find_element_by_id(loc)