# spider for 360doc.com export to excel

import urllib.request, urllib.error
from bs4 import BeautifulSoup
import re
import xlwt

url = "http://www.360doc.com/content/22/1019/06/47068916_1052279257.shtml"
fakeHeaders = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36' }
req = urllib.request.Request(url, headers = fakeHeaders)

try:
	resp = urllib.request.urlopen(req, timeout=10.01)
	print("response code: %s" % (resp.getcode()))
	# print("response header:\n", resp.getheaders())
	byte = resp.read()
	html = byte.decode("utf-8")
	soup = BeautifulSoup(html, features="lxml")

	print("response body:")
	# print(soup.head.contents[1])
	# print(soup.head.title.string)
	# print(soup.body.div)

	# print(soup.findAll("p", string="【原文】"))
	# print(soup.body.findAll("div", attrs={"class": "anony-nav-links"})
	# print(soup.select("#anony-reg-new"))

	findLink = re.compile(r'<a href="(.*?)">')
	findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S)
	titlePattern = re.compile(r'<p>\d')

	dataList = []
	data = []
	artContent = soup.body.find_all("p")
	for item in artContent:
		# item = str(item)
		# title = re.findall(findTitle, item)[0] //匹配不到，报错
		if re.match(titlePattern, str(item)):
			dataList.append(data)
			data = []
			data.append(item.text)
		if str(item).startswith('<p>【原文】'):
			data.append(item.text)
		if str(item).startswith('<p>【组成】'):
			data.append(item.text)
		if str(item).startswith('<p>【功用】'):
			data.append(item.text)
		if str(item).startswith('<p>【煎法】'):
			data.append(item.text)
		if str(item).startswith('<p>【方歌】'):
			data.append(item.text)
	#print(dataList)

	myexcel = xlwt.Workbook(encoding="utf-8", style_compression=0)
	sheet1 = myexcel.add_sheet("sheet1", cell_overwrite_ok=True)
	head = ("名称", "原文", "组成", "功用", "煎法", "方歌")
	for item in head:
		sheet1.write(0, head.index(item), item)
	for data in dataList:
		for d in data:
			sheet1.write(dataList.index(data), data.index(d), d)
	myexcel.save('D:\\PythonProjects\\spider\\myexcel.xls')

except urllib.error.URLError as e:
    print("error occur: ", e)
    if hasattr(e, "code"):
        print(e.code)