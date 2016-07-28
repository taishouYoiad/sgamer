# -*- coding:utf-8 -*-
import re
import urllib
import urllib2
import time

VAILD_TIME = 60 * 60 * 2
#11
user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
headers = {'User-Agent' : user_agent}
regex_url = re.compile(r"</em> <a href=\"(.*?)\.html\".*? onclick=\"atarget\(this\)\" class=\"s xst\">(.*?)</a>\r\n(?:<img.*?\r\n)*.*?>(\d*)</a></span>")
def parse_url(url):
	web_page = []
	try:
		request = urllib2.Request(url, headers = headers)
		response = urllib2.urlopen(request, timeout = 5)
		#page_text = response.read().decode('utf-8')
		page_text = response.read()
		target_subject = regex_url.findall(page_text)
		for subject in target_subject:
			per_page = {"url" : "http://bbs.sgamer.com/" + subject[0] + ".html", "title" : subject[1], "num" : subject[2]}
			web_page.append(per_page)
		return web_page
	except Exception as e:
		print(e)

regex_page = re.compile(r"<td class=\"t_f\" id=\"postmessage_\d*\">(.*?)</td></tr></table>", re.DOTALL)
def parse_page(url):
	try:
		request = urllib2.Request(url, headers = headers)
		response = urllib2.urlopen(request, timeout = 5)
		#page_text = response.read().decode('utf-8')
		page_text = response.read()
		target_subject = regex_page.findall(page_text)
		for subject in target_subject:
			subject = re.sub("<.*?>"," ",subject)
			subject = re.sub("\r\n","",subject)
			if subject not in content:
				check = re.search("\d*-\d*-\d* \d*:\d",subject)
				if(not hasattr(check,"group")):
					content.append(subject)
					print(subject)
	except Exception as e:
		print(e)

regex_time = re.compile("发表于 <span title=\"(\d*-\d*-\d* \d*:\d*:\d*)\">")
def get_topic_time(url):
	try:
		request = urllib2.Request(url, headers = headers)
		response = urllib2.urlopen(request, timeout = 5)
		#page_text = response.read().decode('utf-8')
		page_text = response.read()
		t = regex_time.search(page_text)
		#t = re.search("<em id=.*?<span title=\"(\d*-\d*-\d* \d*:\d*:\d*)\">", page_text)
		if(hasattr(t, "group")):
			topic_time = time.mktime(time.strptime(t.group(1),'%Y-%m-%d %H:%M:%S'))
			return topic_time
		else:
			return 0
	except Exception as e:
		print(e)
	
for x in range(1,20):
	url = "http://bbs.sgamer.com/forum-44-" + str(x) + ".html"
	web_pages = parse_url(url)
	for page in web_pages:
		topic_time = get_topic_time(page["url"])
		if(time.time() - topic_time < VAILD_TIME):
			print(page["title"])
		else:
			print("XXXXXXXXXXXXX" + page["title"])
'''
for x in range(1,20):
	url = "http://bbs.sgamer.com/forum-44-" + str(x) + ".html"
	print(url)
	web_pages = parse_url(url)
	for page in web_pages:
		t_url = page["url"]
		t_title = page["title"]
		t_num = page["num"]
		content = []
		print("=====================================" + t_title + "==========================")
		command = raw_input('>>')
		if(command == "x"):
			for p in range(1,int(t_num)):
				url = re.sub("-1-", "-"+ str(p) +"-", t_url)
				parse_page(url)
		print("================================================================================")
'''
