# Python3
# -*- coding: utf-8 -*-
# LIFO即Last in First Out,后进先出。
# 与栈的类似，使用也很简单,maxsize用法同上
import queue

q = queue.LifoQueue()

for i in range(5):
    q.put(i)

while not q.empty():
    print(q.get())