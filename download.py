# -*- coding: UTF-8 -*-
#download函数可以捕获异常、重试下载num_retries、
#并设置用户代理user_agent
import urllib2
def download(url,user_agent='wswp',num_retries = 2):
	print "Downloading:",url
	headers={'User-agent':user_agent}
	#在引入的urllib2库中调用request函数、用法？
	request = urllib2.Request(url,headers=headers)
	try:
		#在urllib2中调用了urlopen函数
		html = urllib2.urlopen(url).read()
		#
	except urllib2.URLError as e:
		print "Download error:",e.reason
		html = None
		if num_retries >0:
			if hasattr(e,"code") and 500 <= e.code < 600:
			#retry 5XX HTTP errors
				return download(url,user_agent,num_retries-1)

	return html
	


