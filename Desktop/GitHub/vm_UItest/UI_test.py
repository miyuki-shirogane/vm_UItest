#coding=utf-8
'''
@File    :   UI_test.py
@Time    :   2019/12/24 17:23:04
@Author  :   Yilin FEI 
@Contact :   yl.fei@teletraan.io
'''



import sys
sys.path.append("..")
import unittest
from plugin import Browser
from conf import config,switch
from view import LoginView,MemberView,VisitorView,vSettingView,mem_delete,BlacklistView
from plugin import HTMLTestRunner,mylog
import ddt,os,time



@ddt.ddt
class Seely(unittest.TestCase):
 
    @classmethod
    def setUpClass(cls):
        # 打开浏览器和url
        browser = Browser.Browser()
        cls.driver = browser.open_browser()
        cls.lg = LoginView.LoginPage(cls.driver)
        cls.mem = MemberView.MemberPage(cls.driver)
        cls.vst = VisitorView.VisitorPage(cls.driver)
        cls.vset = vSettingView.SettingPage(cls.driver)
        cls.memd = mem_delete.MemberdPage(cls.driver)
        cls.blk = BlacklistView.BlacklistPage(cls.driver)


 
    @classmethod
    def tearDownClass(cls):
        # quit关闭浏览器后，会自动删除临时文件夹，不要用close
        cls.driver.quit()
 
    # 登录用例
    @ddt.data(*config.user_data)
    @ddt.unpack
    def test_1_login(self, account,psw):
        '''登录'''
        self.lg.login(account,psw)

    def test_2_member(self):
        '''员工管理'''
        self.mem.member_add()

    def test_3_visitor(self):
        '''访客管理'''
        self.vst.event_add()



    def test_4_setting(self):
        '''访客设置'''
        self.vset.setting_check()


#针对批量导入大量数据善后用的脚本，不在UI自动化测试之列，一般情况都是注掉的
    # def test_5_memberd(self):
    #     self.memd.member_delete()

    def test_6_setting(self):
        '''黑名单管理'''
        self.blk.blacklist_add()


 
if __name__ == "__main__":
    # unittest执行测试用例，默认是根据ASCII码的顺序加载测试用例
    unittest.main()

