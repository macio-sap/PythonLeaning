#!/usr/bin/python3
import time
import logging
import threading
from threading import Thread

logging.basicConfig(
    level=logging.DEBUG,
    format='%(threadName)-10s: %(message)s',
)   # format 中的 threadName 可以捕获到线程的名字，所以下边logging.debug()中不需要传入线程名

def countdown(n, number):
    while n > 0:
        # print(f'{threading.current_thread().name}-倒数开始：', n)
        logging.debug(f'倒数开始：{n}')
        n -= 1
        time.sleep(1)

def main():
    thread_list = []
    logging.debug('start.....')
    for i in range(3):
        t = Thread(target=countdown, args=(3, i+1))
        t.start()
        thread_list.append(t)  # 把线程放到列表中

    for i in thread_list:   # 终止列表中的线程
        i.join()
    logging.debug('end.....')
if __name__ == '__main__':
    main()