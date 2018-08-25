#-*- coding:utf-8 -*-
import logging  
import time
from cloghandler import ConcurrentRotatingFileHandler
import os
import os.path



class Logger():
    def __init__(self, log_name, logger_name):
        #设置日志文件名称：time.time()取得当前时间；time.localtime()取得本地时间；time.strftime()格式化日期；
        time_str = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime(time.time()))
        logname = time_str + '_' + log_name + '.log'
        
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(level = logging.INFO)
        rHandler = ConcurrentRotatingFileHandler(logname,mode="a",maxBytes = 512*1024,backupCount = 3)
        rHandler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        rHandler.setFormatter(formatter)
   
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        console.setFormatter(formatter)

        self.logger.addHandler(rHandler)
        #self.logger.addHandler(console)
   
    def outputLog(self):
        self.logger.info("Start print log")
        self.logger.debug("Do something debug")
        for i in range(5 + 1):
            self.logger.warning("Do something" + str(i) + "'times....'")
        
        self.logger.warning("Something maybe fail.")  
        self.logger.info("Finish")
        
        
if __name__ == '__main__':
    print(os.getcwd())
    Log = Logger('create_log', "chat.gui.statistic")
    Log.outputLog()
    