# spider for tangnet.cn
# @date 20231109
# @author d
import urllib.request, urllib.error
from bs4 import BeautifulSoup
import re
import random
import time
import xlwt
from snowflake import SnowFlake
from datetime import datetime

baseurl = 'http://www.tangnet.cn'
headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36' }

try:
	req = urllib.request.Request(baseurl + '/novel/63.html#catalog', headers=headers)
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
	sf = SnowFlake(datacenter_id=1, worker_id=1)
	i = 1
	for item in contents:
		item = str(item)
		links = re.findall(findLink, item)
		print(f'目录总条数为：{len(links)}')
		for link in links:
			print(f'开始获取内容{i}: ', end='')
			req1 = urllib.request.Request(baseurl + link, headers=headers)
			resp1 = urllib.request.urlopen(req1, timeout=10.01)
			html1 = resp1.read().decode('utf-8')
			soup1 = BeautifulSoup(html1, features='lxml')
			title1 = soup1.select('.j_chapterName')[0].text
			content1 = ''
			for c in soup1.select('.read-content')[0].select('p'):
				content1 = content1 + str(c)
			data = []
			data.append(sf.get_id())
			data.append(i)
			data.append('伤寒论')
			data.append(title1)
			print(f'{title1}...')
			data.append(content1)
			data.append('0')
			data.append(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
			dataList.append(data)
			sleepTime = random.randint(2, 5)
			time.sleep(sleepTime)
			print('完毕')
			i = i + 1
			# if i > 3:
			# 	break
	# print(dataList)

	myexcel = xlwt.Workbook(encoding="utf-8", style_compression=0)
	sheet1 = myexcel.add_sheet("sheet1", cell_overwrite_ok=True)
	head = ("id", "sort_id", "book_name", "chapter_name", "content_text", 'status', 'create_time')
	for item in head:
		sheet1.write(0, head.index(item), item)
	for data in dataList:
		for d in data:
			sheet1.write(dataList.index(data)+1, data.index(d), d)
	myexcel.save('D:\\PythonProjects\\tangnet.xls')

except urllib.error.URLError as e:
    print('error occur: ', e)
    if hasattr(e, 'code'):
        print(e.code)