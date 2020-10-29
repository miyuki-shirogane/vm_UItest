#coding=utf-8
'''
@File    :   BlacklistView.py
@Time    :   2020/04/28 15:00:06
@Author  :   Yilin FEI 
@Contact :   yl.fei@teletraan.io
'''


'''
页面类：黑名单页
'''

import sys
sys.path.append("..")
from Base_View import BaseView
from plugin.Browser import Browser
import time,os
from conf import config
from plugin import mylog
import pykeyboard
from pykeyboard import PyKeyboard

cur_path = os.path.dirname(os.path.realpath(__file__))
report_path = os.path.join(cur_path,"../report/" + mylog.Date())
if not os.path.exists(report_path):
    os.mkdir(report_path)
log = mylog.mylog(r'%s/UItest_%s.log' %(report_path, mylog.Date()))

# 继承了BaseView类
class BlacklistPage(BaseView):

    # 黑名单
    def blacklist_add(self):
        # global log

        # 进入黑名单管理路径
        log.log('---进入黑名单页')
        self.get_element("Blacklist", "blacklist_sidebar2")
        self.click()

        #断言1
        time.sleep(2)
        if self.current_url() == config.Blacklist_url:
            log.log('---成功进入黑名单页')
        else:
            log.log('---跳转进黑名单页异常，错误见截图','Error')
            self.screenshot()

        #预先获取列表记录数
        self.get_element("Blacklist","blacklist_count")
        i = self.text()
        i = i.split('/')[-1]
        log.log('---当前记录数为'+str(i))


        #填写新增黑名单表单
        log.log('------点击新增黑名单按钮')
        self.get_element("Blacklist","blacklist_add")
        self.click()
        time.sleep(0.5)

        #上传照片
        log.log('------上传照片')
        self.get_element("Blacklist","blacklist_photo")
        self.click()
        time.sleep(0.5)
        k=PyKeyboard()
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
        time.sleep(4)

        #填写其他信息
        log.log('------填写其他信息')

        self.get_element("Blacklist","blacklist_name")
        self.send_key(config.name)


        self.get_element("Blacklist","blacklist_submit")
        self.click()

        time.sleep(5)
        self.get_element("Blacklist","blacklist_count")
        j = self.text()
        j = j.split('/')[-1]

        log.log('---黑名单信息填写、提交完毕!')

        log.log('---当前记录数为'+str(j))


        # time.sleep(2)

        if int(j) == int(i)+1:
            log.log('---新增黑名单成功!')
        else:
            log.log('---新增黑名单异常，错误见截图!','Error')
            self.screenshot()


