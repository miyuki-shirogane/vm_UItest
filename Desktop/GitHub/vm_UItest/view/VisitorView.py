#coding=utf-8
'''
@File    :   VisitorView.py
@Time    :   2019/12/24 16:52:43
@Author  :   Yilin FEI 
@Contact :   yl.fei@teletraan.io
'''


'''
页面类：访客管理页
'''

import sys
sys.path.append("..")
from Base_View import BaseView
from plugin.Browser import Browser
import time,os,random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pykeyboard
from pykeyboard import PyKeyboard
from conf import config
from plugin import mylog




cur_path = os.path.dirname(os.path.realpath(__file__))
report_path = os.path.join(cur_path,"../report/" + mylog.Date())
if not os.path.exists(report_path):
    os.mkdir(report_path)
log = mylog.mylog(r'%s/UItest_%s.log' %(report_path, mylog.Date()))


# 继承了BaseView类
class VisitorPage(BaseView):
    def __init__(self, driver):
 
        # 读取日志
        # self.log = get_log()
        self.driver = driver
    # 访客管理
    def event_add(self):

        # 进入访客管理路径
        log.log('---进入访客记录页')
        self.get_element("Visitor", "visitor_sidebar2")
        self.click()

        #断言1
        time.sleep(5)
        if self.current_url() == config.Visitor_url:
            log.log('---成功进入访客记录页')
        else:
            log.log('---跳转进入访客记录页异常，错误见截图!','Error')
            self.screenshot()

        #预先获取列表记录数
        self.get_element("Visitor","event_count")
        i = self.text()
        i = i.split('/')[-1]
        log.log('---当前记录数为'+str(i))

        #新增event
        log.log('------点击新增访问记录按钮')
        self.get_element("Visitor","event_add")
        self.click()
        time.sleep(2)

        #填写被访人信息
        log.log('------选择被访人')
        self.get_element("Visitor","target_name")
        self.click()
        k=PyKeyboard()
        k.press_key('return')
        k.release_key('return')


        log.log('-----选择来访事由')
        self.get_element("Visitor","reason")
        self.click()
        self.get_element("Visitor","pick_reason")
        self.click()

        log.log('------选择通行权限')
        try:
            self.get_element("Visitor","permission")
            self.click()
            self.get_element("Visitor","pick_permission")
            self.click()
            self.get_element("Visitor","blank")
            self.click()
        except:
            log.log('无法获取权限，请检查是否新增了权限','Warn')

        log.log('------填写权限截止时间')
        self.get_element("Visitor","deadline")
        self.send_key(config.deadline)

        log.log('------填写访客信息')
        self.get_element("Visitor","visitor_name")
        self.send_key(config.name)

        #上传照片
        log.log('------上传照片')
        self.get_element("Visitor","visitor_photo")
        self.click()
        time.sleep(0.5)
        k.press_key('command')
        k.press_key(k.shift_key)
        k.press_key('g')
        k.release_key('command')
        k.release_key(k.shift_key)
        k.release_key('g')
        time.sleep(2)
        k.type_string(config.photo_path)
        time.sleep(5)
        k.press_key('return')
        k.release_key('return')
        time.sleep(2)
        k.press_key('return')
        k.release_key('return')
        time.sleep(2)
        k.press_key('return')
        k.release_key('return')
        # time.sleep(4)
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[3]/div/div[2]/div/form/div[1]/div[19]/div/div/div/div[1]/div/img')))
        except:
            log.log('---访客照片添加异常，见截图','Warn')
            self.screenshot()

        # #添加同行人
        # self.get_element("Visitor","add_partner")
        # self.click()

        # #填写同行人信息
        # log.log('------填写同行人信息')
        # self.get_element("Visitor","p_name")
        # self.send_key(config.p_name)
        # self.get_element("Visitor","p_phone")
        # self.send_key(config.p_phone)
        # self.get_element("Visitor","p_email")
        # self.send_key(config.p_email)


        # self.get_element("Visitor","p_is_notify")
        # self.click()
        # self.get_element("Visitor","p_id_select")
        # self.click()
        # self.get_element("Visitor","p_id_type")
        # self.click()
        # self.get_element("Visitor","p_id_num")
        # self.send_key(config.id_num)
        # self.get_element("Visitor","p_company")
        # self.send_key(config.company)
        # self.get_element("Visitor","p_apartment")
        # self.send_key(config.apartment)
        # self.get_element("Visitor","p_plate")
        # self.send_key(config.plate)
        # self.get_element("Visitor","p_remarks")
        # self.send_key(config.remarks)

        # #上传照片
        # log.log('------上传照片')
        # self.get_element("Visitor","p_photo")
        # self.click()
        # time.sleep(0.5)
        # k.press_key('command')
        # k.press_key(k.shift_key)
        # k.press_key('g')
        # k.release_key('command')
        # k.release_key(k.shift_key)
        # k.release_key('g')
        # time.sleep(2)
        # k.type_string(config.p_visitorPhoto_path)
        # time.sleep(5)
        # k.press_key('return')
        # k.release_key('return')
        # time.sleep(2)
        # k.press_key('return')
        # k.release_key('return')
        # time.sleep(2)
        # k.press_key('return')
        # k.release_key('return')
        # # time.sleep(4)
        # try:
        #     WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[3]/div/div[2]/div/form/div[1]/div[18]/div/div[2]/div/div[1]/div[2]/div/div/div/div/div/div/div[1]/div/div[11]/div/div/label/div/div[1]/img')))
        # except:
        #     log.log('---同行人照片添加异常，见截图','Warn')
        #     self.screenshot()

        # #提交同行人
        # log.log('-----提交同行人')
        # self.get_element("Visitor","sure")
        # self.click()
        # time.sleep(1)

        log.log('-----上传访问事件')
        self.get_element("Visitor","submit")
        self.click()

        time.sleep(5)
        self.get_element("Visitor","event_count")
        j = self.text()
        j = j.split('/')[-1]

        log.log('---上传完毕，当前记录数为'+str(j))

        if int(j) == int(i)+1:
            log.log('---新增访问事件成功!')
        else:
            log.log('---新增异常，错误见截图!','Error')
            self.screenshot()


