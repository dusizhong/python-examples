# spider for tangnet.cn
# @date 20231109
# @author
import urllib.request, urllib.error
from bs4 import BeautifulSoup
import re
import xlwt
import time
import random

url = 'http://www.tangnet.cn/novel/63.html#catalog'
headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36' }
req = urllib.request.Request(url, headers=headers)

try:
	resp = urllib.request.urlopen(req, timeout=10.01)
	print('response code: %s' % (resp.getcode()))
	# print("response header:\n", resp.getheaders())
	byte = resp.read()
	html = byte.decode('utf-8')
	soup = BeautifulSoup(html, features='lxml')

	print('response body:')
	print(soup.head.title.string)
	# contents = soup.select('a')
	# contents = soup.select("#content-tab")
	contents = soup.select('.cate-list')
	# contents = soup.body.find_all('div', attrs={'class': 'cate-list'})
	# print(contents)

	findLink = re.compile(r'<a href="(.*?)" target="_blank">')
	findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S)
	titlePattern = re.compile(r'<p>\d')

	dataList = []
	for item in contents:
		item = str(item)
		links = re.findall(findLink, item)
		for l in links:
			print(l)
		# if len(link) > 0:
		# 	print(link)
		# if str(item).startswith('<div'):
		# 	print(item)
		# 	dataList.append(item)
		# 	print(item)
		# sleepTime = random.randint(2, 5)
		# time.sleep(sleepTime)
	# print(dataList)

except urllib.error.URLError as e:
    print('error occur: ', e)
    if hasattr(e, 'code'):
        print(e.code)