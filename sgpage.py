# -*- coding:utf-8 -*-
import re
import urllib
import urllib2

def parse_url(url):
	user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
	headers = {'User-Agent' : user_agent}
	web_page = []
	try:
		request = urllib2.Request(url, headers = headers)
		response = urllib2.urlopen(request)
		page_text = response.read().decode('utf-8')
		target_subject = re.findall("</em> <a href=\"(.*?)\.html\".*? onclick=\"atarget\(this\)\" class=\"s xst\">(.*?)</a>\r\n.*?>2</a>.*?>(\d*)</a></span>", page_text)
		for subject in target_subject:
			per_page = {"url" : "http://bbs.sgamer.com/" + subject[0] + ".html", "title" : subject[1], "num" : subject[2]}
			web_page.append(per_page)
		#print(web_page)
		return web_page
	except Exception as e:
		print(e)

def parse_page(url):
	user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
	headers = {'User-Agent' : user_agent}
	try:
		request = urllib2.Request(url, headers = headers)
		response = urllib2.urlopen(request)
		page_text = response.read().decode('utf-8')
		target_subject = re.findall("\r\n(.*?)</td></tr></table>", page_text)
		for subject in target_subject:
			if subject not in content:
				content.append(subject)
				print(subject)
	except Exception as e:
		print(e)
		

web_pages = parse_url("http://bbs.sgamer.com/forum-44-1.html")
for page in web_pages:
	t_url = page["url"]
	t_title = page["title"]
	t_num = page["num"]
	content = []
	print("=====================================" + t_title + "==========================")
	for p in range(1,int(t_num)):
		url = re.sub("-1-", "-"+ str(p) +"-", t_url)
		parse_page(url)
	print("================================================================================")
