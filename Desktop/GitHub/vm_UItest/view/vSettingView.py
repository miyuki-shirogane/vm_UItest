#coding=utf-8
'''
@File    :   SettingView.py
@Time    :   2020/01/14 15:43:21
@Author  :   Yilin FEI 
@Contact :   yl.fei@teletraan.io
'''

'''
页面类：访客设置页
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
class SettingPage(BaseView):

    def __init__(self, driver):
        self.driver = driver

    #设置页元素校验
    def setting_check(self):
        log.log('---进入访客设置管理页')

        self.get_element("vSetting", "vSetting_sidebar2")
        self.click()
        # time.sleep(2)
        # try:
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div/div[1]/p')))


#访客表单
        for i in range(1,37,3):
            try:
                if self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div/div[' + str(i) + ']/p').text in config.l:
                    log.log(config.l[(i-1)/3] + '   元素校验正确')
            except:
                log.log('缺少元素   ' + config.l[(i-1)/3],'Error')
                self.screenshot()

        # except:
        #     log.log('---访客设置项加载异常','Error')
        #     self.screenshot()

#
#


if __name__ == "__main__":
    print report_path