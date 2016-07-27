# -*- coding:utf-8 -*-
import re
import urllib
import urllib2

def parse_url(url):
	user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
	headers = {'User-Agent' : user_agent}
	web_page = []
	#regex = re.compile(r"</em> <a href=\"(.*?)\.html\".*? onclick=\"atarget\(this\)\" class=\"s xst\">(.*?)</a>\r\n.*?>(\d*)</a></span>")
	try:
		request = urllib2.Request(url, headers = headers)
		response = urllib2.urlopen(request)
		page_text = response.read().decode('utf-8')
		target_subject = re.findall("</em> <a href=\"(.*?)\.html\".*? onclick=\"atarget\(this\)\" class=\"s xst\">(.*?)</a>\r\n(?:<img.*?/>\r\n)*.*?>(\d*)</a></span>", page_text)
		#target_subject = regex.findall(page_text)
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
	regex = re.compile(r"<td class=\"t_f\" id=\"postmessage_\d*\">(.*?)</td></tr></table>", re.DOTALL)
	try:
		request = urllib2.Request(url, headers = headers)
		response = urllib2.urlopen(request, timeout = 5)
		page_text = response.read().decode('utf-8')
		#target_subject = re.findall("<td class=\"t_f\" id=\"postmessage_\d*\">(.*?)</td></tr></table>", page_text, re.DOTALL)
		target_subject = regex.findall(page_text)
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
