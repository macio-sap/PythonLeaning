import queue
import time

q = queue.Queue()

q.put(2)
q.put(1)
q.put(3)
q.put('python')

print('queue long:%s'%q.qsize())