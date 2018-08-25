#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 使用concurrent.futures模块，这个模块是python3中自带的模块
# 注意 一开始随着线程不断增加，每个线程的第一次执行速度都不快
# 但是，后面明显感到是并行执行
# 另外，启动的线程数超出线程池的上限以后，
# 超出部分明显是在后面执行的，跟首次进入线程池的线程是不同批次执行的
from concurrent.futures import ThreadPoolExecutor
import time

def sayhello(a):
    print("hello: "+a ) # 输出信息
    time.sleep(1)      # 等待两秒钟

def main():
    seed=["张三","李四","王刚",'刘备','关羽','张飞','司马懿','司马昭','司马师']
    start1=time.time()
    for each in seed:
        sayhello(each)
    end1=time.time()
    print("time1 顺序执行: "+str(end1-start1))
    start2=time.time()
    with ThreadPoolExecutor(3) as executor:
        for each in seed:
            executor.submit(sayhello,each)
    end2=time.time()
    print("time2 进程池Submit: "+str(end2-start2))
    start3=time.time()
    with ThreadPoolExecutor(3) as executor1:
        executor1.map(sayhello,seed)
    end3=time.time()
    print("time3 进程池Map: "+str(end3-start3))

if __name__ == '__main__':
    main()