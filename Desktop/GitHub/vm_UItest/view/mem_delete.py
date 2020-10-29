#coding=utf-8
'''
@File    :   mem_delete.py
@Time    :   2020/04/03 16:07:36
@Author  :   Yilin FEI 
@Contact :   yl.fei@teletraan.io
'''

import sys
sys.path.append("..")
from Base_View import BaseView
from plugin.Browser import Browser
import time,os

'''
简单介绍下这个文件实现的功能，主要还是因为人员管理batchUpload有一个小问题；
当文件过大，即导入条目过多时，比如5000条记录会在任务记录里有点问题；那么为了
测试这种情况回去做对应操作。那么每次操作后，你想再试一次，就会需要把前面导的纪录
删掉，但操作db会有很多表关联，且接口删除并不简单，那么还不如利用UI界面来实现这个；
于是就有了这个
'''
class MemberdPage(BaseView):

    # 员工管理
    def member_delete(self):
        # global log

        # 进入员工管理路径

        self.get_element("Member", "member_sidebar1")
        self.click()
        self.get_element("Member", "member_sidebar2")
        self.click()

        #修改分页为100
        self.get_element("Member", "member_pagesize")
        self.click()
        self.get_element("Member", "member_pagesizechoose")
        self.click()

        time.sleep(3)

        for i in range(10):
            self.get_element("Member", "member_checkbox")
            self.click()
            self.get_element("Member", "member_delete")
            self.click()
            self.get_element("Member", "member_deleteconfirm")
            self.click()
            time.sleep(1)
            i = i +1
        time.sleep(3)
        self.get_element("Member", "member_deletetable")
        self.click()
        time.sleep(3)

        self.get_element("Member", "memberd_pagesize")
        self.click()
        self.get_element("Member", "member_pagesizechoose")
        self.click()

        time.sleep(3)

        for i in range(10):
            self.get_element("Member", "memberd_checkbox")
            self.click()
            self.get_element("Member", "memberd_delete")
            self.click()
            self.get_element("Member", "memberd_deleteconfirm")
            self.click()
            time.sleep(1)
            i = i +1