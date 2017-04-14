# -*- coding: UTF-8 -*-
#有四个数字：1、2、3、4，
#能组成多少个互不相同且无重复数字的三位数？各是多少？
#分析：在三位数中的每一位上循环1-4，剔除不合格的

for i in range(1,5):
	for j in range(1,5):
		for k in range(1,5):
			if(i!=j and j!=k and i!=k):
				print i,j,k
