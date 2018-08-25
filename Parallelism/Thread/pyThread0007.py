#!/usr/bin/python3
# 给线程加锁

import time
import logging
import threading
from threading import Thread

logging.basicConfig(
    level=logging.DEBUG,
    format='%(threadName)-10s: %(message)s',
)   # format 中的 threadName 可以捕获到线程的名字，所以下边logging.debug()中不需要传入线程名

def countdown(n):
    while n > 0:
        logging.debug(f'倒数开始：{n}')
        n -= 1
        time.sleep(1)

class MyThread(Thread):
    def __init__(self, name, count):
        Thread.__init__(self)
        self.name = name
        self.count = count

    def run(self):
        try:
            lock.acquire()     # 获取锁
            logging.debug('lock....')
            countdown(self.count)
        finally:
            lock.release()
            logging.debug('open again')

lock = threading.Lock()   # 新建一个锁

def main():
    thread_list = []
    logging.debug('start.....')
    for i in range(3):
        t = MyThread(f'thread-{i+1}', 3)
        t.start()
        thread_list.append(t)  # 把线程放到列表中

    for i in thread_list:   # 终止列表中的线程
        i.join()
    logging.debug('end.....')
if __name__ == '__main__':
    main()