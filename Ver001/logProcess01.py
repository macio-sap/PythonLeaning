#! python3
# -*- coding: utf-8 -*-
import logging.handlers


class clsLog():
    def __init__(self):
        self.log_file_info = r'info.log'
        self.log_file_debug = r'debug.log'
        self.log_file_warning = r'warning.log'
        self.log_file_error = r'error.log'
        self.log_file_critical = r'critical.log'
        handler_info = logging.handlers.RotatingFileHandler(log_file, maxBytes=1024 * 1024, backupCount=5,
                                                   encoding='utf-8')
        handler_debug = logging.handlers.RotatingFileHandler(log_file, maxBytes=1024 * 1024, backupCount=5,
                                                   encoding='utf-8')
        handler_warning  = logging.handlers.RotatingFileHandler(log_file, maxBytes=1024 * 1024, backupCount=5,
                                                   encoding='utf-8')
        handler_error  = logging.handlers.RotatingFileHandler(log_file, maxBytes=1024 * 1024, backupCount=5,
                                                   encoding='utf-8')
        handler_critical = logging.handlers.RotatingFileHandler(log_file, maxBytes=1024 * 1024, backupCount=5,
                                                   encoding='utf-8')
        fmt = '%(asctime)s - %(levelname)s - %(message)s'
        formatter = logging.Formatter(fmt)  # 实例化formatter
        handler.setFormatter(formatter)
        
        loger_info = logging.getLogger('info')
        loger_debug = logging.getLogger('debug')
        loger_warning = logging.getLogger('warning')
        loger_error = logging.getLogger('error')
        loger_critical = logging.getLogger('critical')
        loger_info.addHandler(handler)  # 为logger添加handler
        loger_debug.addHandler(handler)  # 为logger添加handler
        loger_warning.addHandler(handler)  # 为logger添加handler
        loger_error.addHandler(handler)  # 为logger添加handler
        loger_critical.addHandler(handler)  # 为logger添加handler
        loger_info.setLevel(logging.INFO)
        loger_debug.setLevel(logging.DEBUG)
        loger_warning.setLevel(logging.WARINING)
        loger_error.setLevel(logging.ERROR)
        loger_critical.setLevel(logging.CRITICAL)
        listLog = []
        listLog.append(loger_info)
        listLog.append(loger_debug)
        listLog.append(loger_warning)
        listLog.append(loger_error)
        listLog.append(loger_critical)
        return listLog
        
# 定义日志记录相关信息
def set_log():
# logging.debug("debug_msg")
# logging.info("info_msg")
# logging.warning("warning_msg")
# logging.error("error_msg")
# logging.critical("critical_msg")
    log_file: str = r'prog.log'
    handler = logging.handlers.RotatingFileHandler(log_file, maxBytes=1024 * 1024, backupCount=5,
                                                   encoding='utf-8')  # 实例化handler
    fmt = '%(asctime)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(fmt)  # 实例化formatter
    handler.setFormatter(formatter)  # 为handler添加formatter

    logger = logging.getLogger('tst')  # 获取名为tst的logger
    logger.addHandler(handler)  # 为logger添加handler
    logger.setLevel(logging.DEBUG)
    return logger

# 主处理程序过程
def main():
    log = set_log()
    for i in range(10):
    	log.info('检查目录：' + str(i))

# 主要处理
if __name__ == '__main__':
    main()
