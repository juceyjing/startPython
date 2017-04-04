# -*- coding: UTF-8 -*-
from time import sleep
while True:
	raws = int(raw_input("请输入列数："))
	if raws == 0:
		print "stupid input 0!"
		break
	#i控制外层行数 j控制空格的个数 k控制*的个数
	i=j=k=1
	print "等腰直角三角形1"
	for i in range(0,raws):
		for k in range(0,raws-i):
			print "*",
			k+=1
		sleep(0.05)
		i+=1
		print "\n"

