#coding=utf-8
'''
@File    :   Run_Main.py
@Time    :   2019/12/24 17:22:11
@Author  :   Yilin FEI 
@Contact :   yl.fei@teletraan.io
'''




import sys
sys.path.append("..")
import unittest
from plugin.Browser import Browser
from conf import config,switch
from plugin import mylog,HTMLTestRunner
from view import LoginView
import ddt,os,time,sys
# from shutil import make_archive
import shutil
# import zipfile
import smtplib,email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# 当前脚本所在文件真实路径
cur_path = os.path.dirname(os.path.realpath(__file__))
 
def add_case(rule="UI*.py"):
    """第一步：加载所有测试用例"""
    #case_path = os.path.join(cur_path,"src/case") # 用例文件夹 
    case_path = cur_path # 用例文件夹 
    # 定义discover加载所有测试用例
    # case_path：执行用例的目录；pattern：匹配脚本名称的规则；top_level_dir：默认为None
    discover = unittest.defaultTestLoader.discover(case_path,pattern=rule,top_level_dir=None)
    return discover
 
def run_case(all_case):
    """第二步：执行所有的用例，并把结果写入到html测试报告中"""
    now = time.strftime("%Y_%m_%d_%H_%M_%S")
    report_path = os.path.join(cur_path,"report/" + mylog.Date())
    if not os.path.exists(report_path):
        os.mkdir(report_path)
    report_abspath = os.path.join(report_path,now+"result.html")
    print("report path:%s"%report_abspath)
 
    fp = open(report_abspath,"wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title="Seely_UI自动化测试报告结果：",
                                           description="测试代码执行情况")
    if switch.time_switch == '1':
        k=1
        while k<2:
            timing=time.strftime('%H_%M',time.localtime(time.time()))
            if timing == switch.timing_ex:
                print u"开始运行脚本:"
                runner.run(all_case)
                print u"运行完成，退出"
                break
            else:
                time.sleep(5)
                print timing
    else:
        runner.run(all_case)
    fp.close()

def make_archive(source, destination):
        base = os.path.basename(destination)
        name = base.split('.')[0]
        format = base.split('.')[1]
        archive_from = os.path.dirname(source)
        archive_to = os.path.basename(source.strip(os.sep))
        shutil.make_archive(name, format, archive_from, archive_to)
        shutil.move('%s.%s'%(name,format), destination)


def send_mail():
    dir = os.path.join(cur_path,"report")
    file_lists = os.listdir(dir)
    file_lists.sort(key=lambda fn:os.path.getmtime(dir + "/" + fn))
    latest_file = file_lists[-1]

    des = cur_path + '/' + latest_file + '.zip'
    
    make_archive(
        dir + '/' + latest_file,
        des,
    )

    mail_content = '''Hello,
    附件是Seely UI自动化测试报告及日志，请查收
    '''
    message = MIMEMultipart()
    message['From'] = config.sender_address
    message['To'] = config.receiver_address
    message['Subject'] = config.Subject

    message.attach(MIMEText(mail_content, 'text'))
    attach_file = open(cur_path + '/' + latest_file + '.zip', 'rb') # Open the file as binary mode

    payload = MIMEBase('application', 'octate-stream')
    payload.set_payload((attach_file).read())
    encoders.encode_base64(payload) #encode the attachment

    payload.add_header('Content-Disposition', 'attachment', filename='tr.zip')
    message.attach(payload)
    #Create SMTP session for sending the mail
    session = smtplib.SMTP(config.SMTP_server, config.port) #use gmail with port
    session.starttls() #enable security
    session.login(config.sender_address, config.sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(config.sender_address, config.receiver_address, text)
    session.quit()
 

 
if __name__ == '__main__':

    all_case = add_case() # 加载用例
    run_case(all_case)  # 执行用例输出报告
    send_mail()

