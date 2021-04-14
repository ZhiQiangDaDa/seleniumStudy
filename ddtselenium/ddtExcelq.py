#encoding=utf8
import ddt
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
    #获取项目的相对路径
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
    #索引从0 开始
    print ("获取整列内容",table.col_values(0))
    print("获取整行内容",table.row_values(0))

    print( str( table.row_values(row)[1]))
    return table.row_values(row)[1]

#得到excel表中第一个sheet中的第一列数据
def getData():
    path=os.getcwd()
    filename=path+r'\ddtselenium\datainfo2.xlsx'
    excels=xlrd.open_workbook(filename,'r')
    table=excels.sheet_by_index(0)
    #下面是关键，如果不用新表直接返回xlrd读取到的数据，由于格式不同会导致报错
    newRows=[]
    for rowValue in range(1,table.nrows):
        newRows.append(table.row_values(rowValue,0,table.ncols))
    print("新的数组",newRows)
    return newRows


    print(table.col_values(0))
    # return [['1234@1110000.com56'],
    # ['123456sfjowj'],
    # ['weoiwow',],
    # ['weoiwow33333333333333',],
    #  ['weoiwoewew44444444444w',],
    # ]
    return table.col_values(0)
def readData():
    return[['123456','psd','请输入帐号密码'],
    ['123456','','请输入帐号密码'],
    ['','','请输入帐号密码'],

    ]
@ddt.ddt 
class TestBdSearch(unittest.TestCase):
    def setUp(self):
        getData()
        #print("来自",readUserName(3))
        self.driver=webdriver.Chrome()  
        self.url="https://www.baidu.com/"
        self.driver.get(self.url)
        WebDriverWait(self.driver,2)
    def tearDown(self):   
        self.driver.quit()
    @ddt.data(*getData())
    @ddt.unpack
    #，getData（）返回的数组中每一个有多少数据，下面就要写相应个数的参数
    def test_search(self,name,name1,name2):
        # self.driver.find_element_by_id('kw').send_keys(readUserName(1))
            self.driver.find_element_by_id('kw').send_keys(name)
            sleep(3)

if __name__ =='__main__':
    unittest.main()


