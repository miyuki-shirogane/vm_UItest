#coding=utf-8
'''
@File    :   LoginView.py
@Time    :   2019/12/24 16:52:32
@Author  :   Yilin FEI 
@Contact :   yl.fei@teletraan.io
'''


'''
页面类：登录页
'''

import sys
sys.path.append("..")
from Base_View import BaseView
from plugin.Browser import Browser
import time,os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from conf import config
from plugin import mylog



cur_path = os.path.dirname(os.path.realpath(__file__))
report_path = os.path.join(cur_path,"../report/" + mylog.Date())

if not os.path.exists(report_path):
    os.mkdir(report_path)
log = mylog.mylog(r'%s/UItest_%s.log' %(report_path, mylog.Date()))

# 继承了BaseView类
class LoginPage(BaseView):

    def __init__(self, driver):
 
        # 读取日志
        # self.log = get_log()
        self.driver = driver

    # 登录
    def login(self,account,psw):
        # global log

        # 输入账号
        log.log('---登录_输入账号')
        self.get_element("Login", "account")
        self.send_key(account)

        # 输入密码
        log.log('---登录_输入密码')
        self.get_element("Login", "psw")
        self.send_key(psw)

        # 点击登录
        log.log('---登录_点击登录')
        self.get_element("Login", "enter")
        self.click()




        #断言
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="root"]/div/div[1]/div/div/div[1]')))
            log.log('---登录成功！')
        except:
            log.log('---登录异常，错误见截图!','Error')
            self.screenshot()

        self.get_element("Member", "member_sidebar1")
        self.click()

        self.get_element("Visitor", "visitor_sidebar1")
        self.click()

        self.get_element("Blacklist", "blacklist_sidebar1")
        self.click()

if __name__ == "__main__":
    print report_path





