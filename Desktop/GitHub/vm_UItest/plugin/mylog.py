# -*- coding:utf-8 -*-

from timeFormat import timeFormat
import logging, time ,os,datetime



cur_path = os.path.dirname(os.path.realpath(__file__))
report_path = os.path.join(cur_path,"report")
if not os.path.exists(report_path):
    os.mkdir(report_path)
    
class mylog:

    def now(self):
        return int(time.time())
    
    def Now(self):
        return timeFormat(int(time.time()))

    def log(self, msg, level = 'info'):
        level = level.upper()
        if(level == 'WARN'):
            logging.warn(self.Now() + ' '+ msg)
        elif(level == 'ERROR'):
            logging.error(self.Now() + ' '+ msg)
        else:
            logging.info(self.Now() + ' '+ msg)
            
    
    def __init__(self, filename='my.log'):
        logging.basicConfig(level=logging.INFO, filename=filename)
        self.log('page testing started')

    # def __del__(self):
    #     self.log('page testing closed')
        
def Date():
    return timeFormat(int(time.time())).split()[0]


if __name__ == '__main__':
    log = mylog(report_path+r'/test_%s.log' %Date())
    log.log('This is a test for mylog')
    log.log('哦豁','Warn')
    log.log('哎嘿','Error')
    del log


