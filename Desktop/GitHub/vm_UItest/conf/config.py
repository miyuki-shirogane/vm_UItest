#coding=utf-8
'''
@File    :   config.py
@Time    :   2019/12/24 16:53:22
@Author  :   Yilin FEI 
@Contact :   yl.fei@teletraan.io
'''


import random,datetime


#seely test account info
s_address = 'https://seely-test.teletraan.io/app/login/'
Visitor_url = 'https://seely-test.teletraan.io/app/visitor/visitor-log/'
user_data = (("misaki@t.io", "teletraan"),)

#Member test data
Member_url = 'https://seely-test.teletraan.io/app/id-management/member/'

#Visitor test data
photo_path = r'/Users/yilin/Desktop/zz/3234.jpg'
deadline = (datetime.datetime.now()+datetime.timedelta(hours=3)).strftime("%Y%m%d%H%M")

name = 'autoUIName'+str(random.randint(100,999))
serialNumber = str(random.randint(1000,9999))
email = 'autoUIemail'+str(random.randint(100,999)) + '@t.io'


#Visitor Setting test data
l = [u'访客照片',u'所在部门',u'预约时间',u'权限截止时间',u'访客姓名',u'手机号码',u'电子邮件',u'所在公司',u'来访事由',u'帐号组权限',u'证件号码',u'备注']


Blacklist_url = 'https://seely-test.teletraan.io/app/blacklist/blacklist-table/'




#mail_date
sender_address = 'sales@scanvis-ai.com'
sender_pass = 'tQS@^V!P92'
receiver_address = 'miyuk1@126.com'
Subject = 'Seely UItest Result'
SMTP_server = 'smtp.office365.com'
port = 587