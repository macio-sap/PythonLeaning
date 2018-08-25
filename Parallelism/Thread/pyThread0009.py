#!/usr/bin/python3
# 出现锁嵌套时，要用threading.RLock建立锁，否则程序会出问题
import time
import logging
import threading
import random
import sys
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

# lock = threading.Lock()   # 新建一个锁
lock = threading.RLock()   # 可以用于锁嵌套
TOTAL = 0

def add_plus_3():
    global TOTAL
    with lock:
        TOTAL += 3

def add_plus():
    global TOTAL
    with lock:        # 锁的新用法，用完之后可以自动关闭
        logging.debug(f'before add:{TOTAL}')
        wait = random.randint(1, 3)
        time.sleep(wait)
        print(f'执行了{wait}s之后。。。')
        TOTAL += 1
        logging.debug(f'after add:{TOTAL}')
        add_plus_3()

def main():
    thread_list = []
    logging.debug('start.....')
    for i in range(int(sys.argv[1])):
        t = Thread(target=add_plus)
        t.start()
        thread_list.append(t)  # 把线程放到列表中
    for i in thread_list:   # 终止列表中的线程
        i.join()
    logging.debug('end.....')
if __name__ == '__main__':
    main()