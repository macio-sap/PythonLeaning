#!/usr/bin/python3

import time
from threading import Thread

def countdown(n):
    while n > 0:
        print('倒数开始：', n)
        n -= 1
        time.sleep(1)

def main():
    t = Thread(target=countdown, args=(5, ))   # target=函数名，args=() 给target=的函数传参数，参数以元组形式传，如果只有一个，要加逗号
    t.start()                                  # 启动线程

if __name__ == '__main__':
    main()