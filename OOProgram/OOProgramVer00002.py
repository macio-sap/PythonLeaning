# Python3
# -*- coding: utf-8 -*-


n = 0


# 验证全局变量和本地变量的差异
class Cls01():
	def __init__(self):
		global n
		self.n = n # 将全局变量n 的值复制给类的本地变量
		self.n += 1 # 修改本地变量的信息
		print(n)    # 显示全局变量n的值 应该是0
		print(self.n) # 显示本地变量的值，应该是修改后的1
		


def main():
	Cls01()


if __name__ == '__main__':
	main()