# 用I/O操作来检测多线程与非多线程处理任务所花的时间
# 测试多线程是否适合I/O密集型，用时间加减来检测多线程与非多线程
#!/usr/bin/python3
import time
from queue import Queue    # 用队列来保存线程的结果，先进先出
from threading import Thread
import requests

q_result = Queue()  # 新建一个队列对象
urls = [
    "http://www.baidu.com",
    "http://www.qq.com",
    "http://www.360.com",
    "http://www.baidu.com",
    "http://www.qq.com",
    "http://www.360.com",
    "http://www.baidu.com",
    "http://www.qq.com",
    "http://www.360.com",
]

def get_page(url, queue):
    result = requests.get(url).content   # 获取页面内容
    queue.put(result[:10])   # 保存前10个字符
    with open('utl.txt', 'ab') as f:
        f.write(result[:100])

def with_thread():
    thread_list = []
    start_time = time.time()
    for s in urls:
        t = Thread(target=get_page, args=(s, q_result))
        t.start()
        thread_list.append(t)

    for i in thread_list:
        i.join()
    print('with thread:', (time.time() - start_time) * 1000)   # 显示毫秒
    return [q_result.get() for _ in range(len(urls))]

def no_thread():
    start_time = time.time()
    q = Queue()
    for s in urls:
        get_page(s, q)

    print('no thread:', (time.time() - start_time) * 1000)   # 显示毫秒
    return [q.get() for _ in range(len(urls))]

def main():
    print(no_thread())  # 打印return的内容
    print(with_thread())

if __name__ == '__main__':
    main()