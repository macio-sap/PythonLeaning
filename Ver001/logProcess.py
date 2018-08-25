#! python3
# -*- coding: utf-8 -*-
import logging.handlers


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
