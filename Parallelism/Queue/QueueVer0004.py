import queue
import time

q = queue.Queue()
que = queue.Queue()

q.put(2)
q.put(1)
q.put(3)
q.put('python')

print('q is empty? :%s'%q.empty())
print('que is empty? :%s'%que.empty())


while not q.empty():
    next_item = q.get()
    print('q is empty? :%s' % q.empty())
    print(next_item)
    time.sleep(.5)


print('que is empty? :%s'%que.empty())
