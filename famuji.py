# -*- coding:utf-8 -*-
import urllib
import urllib2
import time
import sgamer
import re
import MySQLdb
import random

accept = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8" 
acceptencoding = "gzip, deflate"
acceptlanguage = "zh-CN,zh;q=0.8"
contenttype = "application/x-www-form-urlencoded"
host = "bbs.sgamer.com"
origin = "http://bbs.sgamer.com"
agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
referer = "http://bbs.sgamer.com/thread-13096834-1-3.html"
cookie = "U6IV_2132_saltkey=ola806kX; U6IV_2132_lastvisit=1469594886; U6IV_2132_atarget=1; U6IV_2132_visitedfid=44; U6IV_2132_client_created=1469626672; U6IV_2132_client_token=182995B263F03F81757371371C65CCEE; U6IV_2132_connect_login=1; U6IV_2132_connect_uin=182995B263F03F81757371371C65CCEE; U6IV_2132_auth=abb13RBJbGIV9wDuMDz0KNhwQwKLKJ2jCS7RwV66k3PXEezpN1UZD5aTPxai%2B884SgE4aQ6CNgStP4M%2FOB8LBryXK9FR; pgv_pvi=169183000; U6IV_2132_security_cookiereport=83e0EEL2Onv2vdjdQXEmWfm23vQggItilrwnJVHIJEKDC4WSfKH%2B; U6IV_2132_connect_last_report_time=2016-08-01; U6IV_2132_home_diymode=1; U6IV_2132_connect_sync_post=13096751%7C43748760; U6IV_2132_ulastactivity=1470056824%7C0; U6IV_2132_st_t=8403274%7C1470056868%7C9b5495b15cdb5fc78383e7fa9ad9e25e; U6IV_2132_forum_lastvisit=D_44_1470056868; U6IV_2132_connect_not_sync_t=1; U6IV_2132_st_p=8403274%7C1470057119%7C3d3a147eda27f12dfa0ee401a37eef1f; U6IV_2132_viewid=tid_13096630; U6IV_2132_smile=1D1; CNZZDATA30039357=cnzz_eid%3D1827369796-1435920789-http%253A%252F%252Fwww.sgamer.com%252F%26ntime%3D1470054946; U6IV_2132_lastact=1470057143%09forum.php%09ajax; U6IV_2132_connect_is_bind=1"
cookie = "U6IV_2132_saltkey=IMgTr1tt; U6IV_2132_lastvisit=1469026827; U6IV_2132_atarget=1; U6IV_2132_client_created=1469030735; U6IV_2132_client_token=182995B263F03F81757371371C65CCEE; U6IV_2132_connect_login=1; U6IV_2132_connect_uin=182995B263F03F81757371371C65CCEE; U6IV_2132_auth=df06j%2B5pGHEgoa1cIVkLZIUqLTFKNxvF084QZxbuptVqNoErHIu8K%2B8N7HyzguI5nR%2B9bxpPHm6FDywDhW7IhLc6LY2S; U6IV_2132_newemail=8403274%09zhukai01%40qq.com%091470065438; U6IV_2132_resendemail=1470065438; U6IV_2132_visitedfid=44D142D40; U6IV_2132_home_diymode=1; U6IV_2132_security_cookiereport=5b66NRO70QNsXlRHoLfnORj1DacqQVQ2XN%2BlLYoiDImKzVV9BBb7; U6IV_2132_connect_last_report_time=2016-08-02; U6IV_2132_ulastactivity=1470070653%7C0; U6IV_2132_sendmail=1; U6IV_2132_connect_not_sync_t=1; U6IV_2132_st_t=8403274%7C1470070701%7C69e27af76c2d3d53c1680e8154133fc6; U6IV_2132_forum_lastvisit=D_40_1469552781D_142_1470065429D_44_1470070701; U6IV_2132_st_p=8403274%7C1470070894%7Ca62b6dc706a94a61ed5cb4a0c6627258; U6IV_2132_viewid=tid_13096997; U6IV_2132_checkpm=1; CNZZDATA30039357=cnzz_eid%3D1353081044-1467735902-%26ntime%3D1470065746; U6IV_2132_noticeTitle=1; U6IV_2132_smile=5D1; U6IV_2132_lastact=1470070902%09forum.php%09ajax; U6IV_2132_connect_is_bind=1"

regex_url = re.compile(r"</em> <a href=\"(.*?)-1-\d*\.html\" onclick=\"atarget\(this\)\" class=\"s xst\">(.*?)</a>\r\n")
def parse_url(url):
	web_page = []
	try:
		headers_no_zip = {"Accept":accept,"Accept-Language":acceptlanguage,"Content-Type":contenttype,"Host":host,"User-Agent":agent,"Origin":origin,"Referer":referer}
		request = urllib2.Request(url, headers = headers_no_zip)
		response = urllib2.urlopen(request, timeout = 5)
		page_text = response.read()
		target_subject = regex_url.findall(page_text)
		for subject in target_subject:
			per_page = {"url" : subject[0], "title" : subject[1]}
			web_page.append(per_page)
		return web_page
	except Exception as e:
		print(e)

def get_hash_key(url):
	headers_no_zip = {"Accept":accept,"Accept-Language":acceptlanguage,"Content-Type":contenttype,"Host":host,"User-Agent":agent,"Origin":origin,"Referer":referer}
	request = urllib2.Request(url, headers = headers_no_zip)
	response = urllib2.urlopen(request)
	text = response.read()
	hashkey = re.search('name="formhash" value="(.*?)"', text)
	return hashkey.group(1)

def get_reply(url):
	request = urllib2.Request(url)
	response = urllib2.urlopen(request)
	text = response.read()
	reply = re.search('postmessage_\d*\">\r\n(.*?)</td></tr></table>', text)
	if(not hasattr(reply,"group")):
		return "famufamufamu~~~"
	else:
		bug = ""
		for i in range(1,10):
			bug = bug +random.choice('abcdefghijklmnopqrstuvwxyz!@#$%^&*()')
		return "\r\n" + reply.group(1) + bug

conn = MySQLdb.connect(host = 'localhost', user = 'root', passwd = '123456', db = 'sgamer', port = 3306)
cur = conn.cursor()
while(1):
	for index in range(1,100):
		p_url = "http://bbs.sgamer.com/forum-44-" + str(index) + ".html"
		web_pages = parse_url(p_url)
		for page in web_pages:
			print(page["url"])
			sql = "select * from famu where url=\"" + page["url"] + "\" limit 1"
			res = cur.execute(sql)
			if res == 1:
				continue
			else:
				sql = "insert into famu (url,time) values(\"" + page["url"] + "\"," + str(int(time.time())) +  ")"
				cur.execute(sql)
				conn.commit()

			headers = {"Accept":accept,"Accept-Encoding":acceptencoding,"Accept-Language":acceptlanguage,"Content-Type":contenttype,"Host":host,"User-Agent":agent,"Origin":origin,"Referer":referer,"Cookie":cookie}

			url = "http://bbs.sgamer.com/" + page["url"] + "-1-1.html"
			hashkey = get_hash_key(url)
			tid = re.search("thread-(\d+)", page["url"]).group(1)
			post_url = "http://bbs.sgamer.com/forum.php?mod=post&action=reply&fid=44&tid=" + str(tid) + "&extra=page%3D3&replysubmit=yes&infloat=yes&handlekey=fastpost&inajax=1"

			message = get_reply(url)
			print(message)	
			curr_time = int(time.time())
			data = {"message":message,"posttime":curr_time,"formhash":"38fa531b","usesig":1,"subject":"","connect_publish_t":0}
			postdata = urllib.urlencode(data)
			request = urllib2.Request(post_url, postdata, headers)
			response = urllib2.urlopen(request)
			for i in response:
				print(i)
			rnd = random.randint(2,10)
			time.sleep(16 + rnd)
cur.close()
conn.close()
