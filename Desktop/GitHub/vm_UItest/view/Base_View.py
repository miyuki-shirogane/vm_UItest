#coding=utf-8
'''
@File    :   Base_View.py
@Time    :   2019/12/24 16:52:21
@Author  :   Yilin FEI 
@Contact :   yl.fei@teletraan.io
'''


'''
基本类
'''

import sys
sys.path.append("..")
from time import sleep
from xml.etree import ElementTree
from selenium.common.exceptions import NoSuchElementException
import os
import time
import csv
from plugin import mylog


 

cur_path = os.path.dirname(os.path.realpath(__file__))
report_path = os.path.join(cur_path,"../report/" + mylog.Date())

class BaseView(object):
 
    # 初始化driver
    def __init__(self, driver):
 
        # 读取日志
        # self.log = get_log()
        self.driver = driver
 
    # 从xml文件读取元素
    def set_xml(self):
        self.activity = {}
        if len(self.activity) == 0:
 
            # 获取配置文件
            cur_path = os.path.abspath(os.path.dirname(os.getcwd()))
            file_path = os.path.join(cur_path,'vm_UItest/conf/Elm_Mng.xml')
            tree = ElementTree.parse(file_path)
            # 从activity标签开始遍历
            for ac in tree.findall("activity"):
                ac_name = ac.get("name")
                element = {}
                for el in list(ac):
                    element_id = el.get("id")
                    name = {}
                    for data in list(el):
                        name[data.tag] = data.text
                    element[element_id] = name
                self.activity[ac_name] = element
 
    # 把需要获取的元素信息放在字典里
    def get_el_dict(self, activity_name, element_name):
        self.set_xml()
        activity_dict = self.activity.get(activity_name).get(element_name)
        return activity_dict
 
    # 获取具体的元素值，并赋值给两个全局变量，方便其他函数调用
    def get_element(self, activity_name, element_name):
        self.activity = activity_name
        self.element = element_name
        
        element_dict = self.get_el_dict(self.activity, self.element)
        self.pathType = element_dict.get('pathType')
        self.pathValue = element_dict.get("pathValue")
 
    # 判断元素是否存在
    # def is_exist(self):
    #     try:
    #         if self.pathType == 'ID':
    #             self.driver.find_element_by_id(self.pathValue)
    #             return True
    #         if self.pathType == 'XPATH':
    #             self.driver.find_element_by_xpath(self.pathValue)
    #             return True
    #         if self.pathType == 'CLASSNAME':
    #             self.driver.find_element_by_class_name(self.pathValue)
    #             return True
    #         if self.pathType == 'NAME':
    #             self.driver.find_element_by_name(self.pathValue)
    #             return True
    #         if self.pathType == 'LinkText':
    #             self.driver.find_element_by_link_text(self.pathValue)
    #             return True
    #     except NoSuchElementException:
    #         return False



    # 定位元素
    def locate_element(self):
        try:
            if self.pathType == 'ID':
                element = self.driver.find_element_by_id(self.pathValue)
                return element
            if self.pathType == 'XPATH':
                element = self.driver.find_element_by_xpath(self.pathValue)
                return element
            if self.pathType == 'CLASSNAME':
                element = self.driver.find_element_by_class_name(self.pathValue)
                return element
            if self.pathType == 'NAME':
                element = self.driver.find_element_by_name(self.pathValue)
                return element
            if self.pathType == 'LinkText':
                element = self.driver.find_element_by_link_text(self.pathValue)
                return element
            if self.pathType == "IFRAME":
                self.driver.switch_to.frame(self.pathValue)
 
        except NoSuchElementException:
                return None
 


    #获取当前url
    def current_url(self):
        sleep(0.5)
        profile_url =  self.driver.current_url
        return profile_url

    # 截图
    def screenshot(self):
        sleep(0.5)
        self.driver.get_screenshot_as_file(report_path  + '/screenshot'+str(time.time())+'.png')

 
    # 点击
    def click(self):
        element = self.locate_element()
        sleep(0.5)
        element.click()
 
    # 输入
    def send_key(self, key):
        element = self.locate_element()
        sleep(0.5)
        element.clear()
        element.send_keys(key)


    #text
    def text(self):
        element = self.locate_element()
        sleep(0.5)
        return element.text        















