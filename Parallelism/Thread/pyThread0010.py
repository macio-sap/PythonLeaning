# 取得线程中的结果
from queue import Queue    # 用队列来保存线程的结果，先进先出
from threading import Thread
import time
import logging

q_result = Queue()  # 新建一个队列对象
str_list = ['1', '3', '6', '8']

logging.basicConfig(
    level=logging.DEBUG,
    format='%(threadName)-10s: %(message)s',
)   # format 中的 threadName 

def str_to_int(arg, queue):
    result = int(arg)         # 将列表中的字符串转换成数字
    queue.put({arg: result})
    logging.debug('倒数开始：{result}')
    time.sleep(5)

def main():
    thread_list = []
    for s in str_list:
        t = Thread(target=str_to_int, args=(s, q_result))
        t.start()
        thread_list.append(t)

    for i in thread_list:
        i.join()

    return [q_result.get() for _ in range(len(str_list))]    # 列表生成式，等同于上边的for循环

if __name__ == '__main__':
    print(main())   # 打印main()中的return 内容