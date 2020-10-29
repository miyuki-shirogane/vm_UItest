# -*- coding: utf-8 -*-
# 时间格式转化
# 支持 绝对秒 与 YYYY-MM-DD HH:mm:ss格式的字符串 相互转换
# 直接调用timeFormat()即可，无需指定格式（多态的体现）
# 已注代码为class版本，因嫌弃通过对象调用有点麻烦，同时参考标准库的功能实现，改成了函数实现

from time import strftime,localtime,mktime,strptime,time

#long转string
def __ltstr(t):
   return strftime("%Y-%m-%d %H:%M:%S",localtime(t))

#string转long
def __strtl(t):
   return int(mktime(strptime(t,"%Y-%m-%d %H:%M:%S")))

def timeFormat(t):
   #利用异常捕捉实现多态处理
   try:
      t = int(t)
      return __ltstr(t)
   except:
      try:
         t = t.strip()
         return __strtl(t)
      except:
         return t

def now():
   return int(time())

def Now():
   return timeFormat(now())

def test():
   print now()
   print Now()

if __name__ == '__main__':
    test()
