# -*- coding:utf-8 -*-
import re
import urllib
import urllib2
import time
import MySQLdb

class sgamer:
	def __init__(self):
		self.VAILD_TIME = 60 * 60 * 24
		user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
		self.headers = {'User-Agent' : user_agent}
		self.regex_url = re.compile(r"</em> <a href=\"(.*?)-1-\d*\.html\".*? onclick=\"atarget\(this\)\" class=\"s xst\">(.*?)</a>\r\n(?:<img.*?\r\n)*.*?>(\d*)</a></span>")
		self.regex_page = re.compile(r"<td class=\"t_f\" id=\"postmessage_\d*\">(.*?)</td></tr></table>", re.DOTALL)
		self.regex_time = re.compile("发表于 <span title=\"(\d*-\d*-\d* \d*:\d*:\d*)\">")

	def parse_url(self, url):
		web_page = []
		try:
			request = urllib2.Request(url, headers = self.headers)
			response = urllib2.urlopen(request, timeout = 5)
			#page_text = response.read().decode('utf-8')
			page_text = response.read()
			target_subject = self.regex_url.findall(page_text)
			for subject in target_subject:
				per_page = {"url" : subject[0], "title" : subject[1], "num" : subject[2]}
				web_page.append(per_page)
			return web_page
		except Exception as e:
			print(e)

	def parse_page(self, url):
		try:
			request = urllib2.Request(url, headers = self.headers)
			response = urllib2.urlopen(request, timeout = 5)
			#page_text = response.read().decode('utf-8')
			page_text = response.read()
			target_subject = self.regex_page.findall(page_text)
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

	def get_topic_time(self, url):
		try:
			request = urllib2.Request(url, headers = self.headers)
			response = urllib2.urlopen(request, timeout = 5)
			#page_text = response.read().decode('utf-8')
			page_text = response.read()
			t = self.regex_time.search(page_text)
			if(hasattr(t, "group")):
				topic_time = time.mktime(time.strptime(t.group(1),'%Y-%m-%d %H:%M:%S'))
				return topic_time
			else:
				return 0
		except Exception as e:
			print(e)
		return 0

