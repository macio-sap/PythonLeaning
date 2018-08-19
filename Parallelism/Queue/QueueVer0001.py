# Python3
# -*- coding: utf-8 -*-
# LIFO即Last in First Out,后进先出。
# 与栈的类似，使用也很简单,maxsize用法同上
import queue
import time
import threading
import operator


# 测试一个后进先出队列的处理方式
class QueueLifo:
    def __init__(self):
        self.qu = queue.LifoQueue()
        # pass
        return

    def put(self):
        for i in range(5):
            self.qu.put(i)

    def print(self):
        print('--- 输出后进先出展示效果：-------------------\r')
        while not self.qu.empty():
            print(self.qu.get())


# 测试一个先进先出队列的处理方式
class QueueFifo:
    def __init__(self):
        self.q = queue.Queue()
        pass
        return

    def put(self):
        for i in range(5):
            self.q.put(i)

    def print(self):
        print('--- 输出先进先出展示效果：-------------------')
        while not self.q.empty():
            print(self.q.get())


class Job(object):
    def __init__(self, priority, description):
        self.priority = priority
        self.description = description
        print('向队列插入节点:',description)
        time.sleep(0.1)
        return

    # 重构ge方法
    def __ge__(self, other):
         return operator.ge(self.priority, other.priority)

    # 重构gt方法
    def __gt__(self, other):
         return operator.gt(self.priority, other.priority)


# 测试一个优先级队列的处理方式
class QueuePriority(object):
    def __init__(self):
        self.q = queue.PriorityQueue()
        pass
        return

    def put(self):
        self.q.put(Job(3, 'level 3 job'))
        self.q.put(Job(10, 'level 10 job'))
        self.q.put(Job(1, 'level 1 job'))
        self.q.put(Job(5, 'level 5 job'))
        self.q.put(Job(4, 'level 4 job'))
        self.q.put(Job(9, 'level 9 job'))
        self.q.put(Job(2, 'level 2 job'))
        self.q.put(Job(6, 'level 6 job'))
        self.q.put(Job(7, 'level 7 job'))
        self.q.put(Job(8, 'level 8 job'))
        self.q.put(Job(11, 'level 11 job'))

    def print(self):
        print('--- 输出先进先出展示效果：-------------------')
        while not self.q.empty():
            print(self.q.get())


class TstPriorityQueue:
    def __init__(self, q):
        self.q = q

    @staticmethod
    def process_job(q):
        while True:
            next_job = q.get()
            desc = '从队列中读取:' + str(next_job.description)
            print(desc)
            time.sleep(1)
            q.task_done()

    def run(self):
        workers = [threading.Thread(target=self.process_job, args=(self.q,)),
                   threading.Thread(target=self.process_job, args=(self.q,)),
                   threading.Thread(target=self.process_job, args=(self.q,)),
                   threading.Thread(target=self.process_job, args=(self.q,)),
                   threading.Thread(target=self.process_job, args=(self.q,))
                   ]

        for w in workers:
            w.setDaemon(True)
            w.start()

        self.q.join()

def main():
    q_fifo = QueueFifo()

    q_fifo.put()
    q_fifo.print()

    q_lifo = QueueLifo()
    q_lifo.put()
    q_lifo.print()


    q_prio = QueuePriority()
    q_prio.put()
    tst = TstPriorityQueue(q_prio.q)
    tst.run()

if __name__ == '__main__':
    main()
