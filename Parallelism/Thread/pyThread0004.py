#!/usr/bin/python3
# 当前线程结束后再执行下一个
import time
import threading
from threading import Thread

def countdown(n, number):
    while n > 0:
        print(f'第{number}个线程，倒数开始：', threading.current_thread().name, n)
        n -= 1
        time.sleep(1)

def main():
    for i in range(3):
        t = Thread(target=countdown, args=(3, i+1))
        t.start()
        t.join()    # waite until the thread terminates 前面线程结束之后再执行下一个

if __name__ == '__main__':
    main()