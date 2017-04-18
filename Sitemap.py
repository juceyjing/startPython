# -*- coding: UTF-8 -*-
from download import download
import re
def crawl_sitemap(url):
	sitemap = download(url)
	#用一个简单的正则表达式，从loc标签中提取出URL
	links=re.findall('<loc>(.*?)</loc>',sitemap)
	#download each link
	for link in links:
		html = download(link)

crawl_sitemap("http://example.webscraping.com/sitemap.xml")

	