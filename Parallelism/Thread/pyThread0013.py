#!/usr/bin/python3
# 线程池的使用
from concurrent.futures import ThreadPoolExecutor, as_completed
import logging
import requests
import time

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

logging.basicConfig(
    level=logging.DEBUG,
    format='%(threadName)-10s: %(message)s',
)

def download(url):
    r = requests.get(url)
    return url, r.status_code

def main():
    with ThreadPoolExecutor(11, thread_name_prefix='yhyang') as executor:
        time.sleep(5)
        # 创建一个5个线程的池
        # 方法1：
        # futures = [executor.submit(download, url) for url in urls]
        # submit 返回一个future对象，futures值为一个包含多个future对象的列表
        # for future in as_completed(futures):
        #     # as_completed(futures) 得到一个可迭代的对象
        #     try:
        #         print(future.result())
        #     except Exception as e:
        #         print(e)

        # 方法2：map() 是对方法1中 submit()的一个封装，简化了使用方法
        futures_result = executor.map(download, urls, timeout=30)
        for future in futures_result:
            try:
                print(future)
                
            except Exception as e:
                print(e)

if __name__ == '__main__':
    main()