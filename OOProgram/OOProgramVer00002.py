# Python3
# -*- coding: utf-8 -*-


n = 0


class Cls01():
	def __init__(self):
		global n
		self.n = n
		self.n += 1
		print(n)
		print(self.n)
		


def main():
	Cls01()


if __name__ == '__main__':
	main()