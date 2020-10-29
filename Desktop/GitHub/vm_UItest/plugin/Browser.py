#coding=utf-8
'''
@File    :   Browser.py
@Time    :   2019/12/24 16:53:13
@Author  :   Yilin FEI 
@Contact :   yl.fei@teletraan.io
'''


import sys,os
sys.path.append("..")
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from conf import config
from plugin import mylog



cur_path = os.path.dirname(os.path.realpath(__file__))
report_path = os.path.join(cur_path,"../report/" + mylog.Date())
if not os.path.exists(report_path):
    os.mkdir(report_path)
log = mylog.mylog(r'%s/UItest_%s.log' %(report_path, mylog.Date()))
class Browser(object):
 

 
    # 打开浏览器
    def open_browser(self):
        # chrome_options = Options()
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome()
        # ,chrome_options=chrome_options
        url = config.s_address
        self.driver.get(url)
        if(1) : self.driver.maximize_window()
        else : self.driver.set_window_size(1440,900)
        return self.driver
 

 
    # 关闭浏览器
    def close_browser(self):
        # quit关闭浏览器后，会自动删除临时文件夹，不要用close
        log.log('关闭Chrome')
        self.driver.quit()


