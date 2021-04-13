#encoding=utf8
import xlrd
from xlrd import open_workbook
import os
import ddt, unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def readUserName(row):
    #filename=r'E:\pyy\ddtselenium\datainfo2.xlsx'
    #filename="datainfo2.xlsx"
    # fullpath = os.path.abspath('..\ddtselenium\datainfo2.xlsx')
    path=os.getcwd()
    filename=path+r'\ddtselenium\datainfo2.xlsx'
    excels=open_workbook(filename,'r')

    sheetNames=excels.sheet_names()
    print(sheetNames)


    #根据索引得到excel第一个sheet中的数据
    table=excels.sheet_by_index(0)
    #这是读到了一行
    print(table.row_values(row))
    for sheet in sheetNames:
        tb=excels.sheet_by_name(sheet)
    #这是一个sheet中的内容 
    print("单页sheet内容",tb)
    
    print(table.row_values)
    #excel 的行数
    print(table.nrows)
    #索引是从0 开始的，及一般情况下excel的第一行为表头，从第一行开始读取数据 按照相应的规则排列即可
    #TODO 怎么样遍历第一列的所有数据呢?
    print( str( table.row_values(row)[1]))
    return table.row_values(row)[1]



class TestBdSearch(unittest.TestCase):
    def setUp(self):
        #print("来自",readUserName(3))
        self.driver=webdriver.Chrome()  
        self.url="https://www.baidu.com/"
        self.driver.get(self.url)
        WebDriverWait(self.driver,2)
    def tearDown(self):
       
         self.driver.quit()
    def test_search(self):
        self.driver.find_element_by_id('kw').send_keys(readUserName(1))
        sleep(3)

if __name__ =='__main__':
    unittest.main()


