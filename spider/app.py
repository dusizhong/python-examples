# spider
import urllib.request, urllib.error
from bs4 import BeautifulSoup

# url = "http://www.baidu.com"
url = "http://douban.com" # need fake header

# fake header
myheaders = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36' }
req = urllib.request.Request(url, headers=myheaders)

# do request
try:
	resp = urllib.request.urlopen(req, timeout=10.01)
	print("response code: %s" % (resp.getcode()))
	# print("response header:\n", resp.getheaders())
	byte = resp.read()
	html = byte.decode("utf-8")
	soup = BeautifulSoup(html, features="lxml")
	print("response body:")
	print(soup.head.contents[1])
	print(soup.head.title.string)
	print(soup.body.findAll(id="anony-nav-banner"))
	print(soup.body.findAll("div", attrs={"class": "anony-nav-links"}))
	print(soup.findAll("div", string="豆瓣电影"))
	print(soup.select("#anony-reg-new"))
except urllib.error.URLError as e:
    print("error occur: ", e)
    if hasattr(e, "code"):
        print(e.code)