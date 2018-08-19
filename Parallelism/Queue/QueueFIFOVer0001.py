# Python3
# -*- coding: utf-8 -*-
# FIFO即First in First Out,先进先出。
# Queue提供了一个基本的FIFO容器，使用方法很简单,maxsize是个整数，
# 指明了队列中能存放的数据个数的上限。一旦达到上限，插入会导致阻塞，
# 直到队列中的数据被消费掉。如果maxsize小于或者等于0，队列大小没有限制。
import queue

q = queue.Queue()

for i in range(10):
    q.put(i)

while not q.empty():
    print(q.get())