import time
import MySQLdb
import sgamer

VAILD_TIME = 60 * 60 * 24

sg = sgamer.sgamer()

try:
	conn = MySQLdb.connect(host = 'localhost', user = 'root', passwd = '123456', db = 'sgamer', port = 3306)
	cur = conn.cursor()
except Exception as e:
	print(e)
for x in range(1,20):
	url = "http://bbs.sgamer.com/forum-44-" + str(x) + ".html"
	web_pages = sg.parse_url(url)
	for page in web_pages:
		true_url = "http://bbs.sgamer.com/" + page['url'] + "-1-1.html"
		topic_time = sg.get_topic_time(true_url)
		if(time.time() - topic_time < VAILD_TIME):
			sql = 'insert into web (url,page_num,time) values("' + page['url'] + '",' + str(page['num']) + ',' + str(int(topic_time))  + ') ON DUPLICATE KEY UPDATE page_num = ' + str(page['num'])  + ''
			cur.execute(sql)
conn.commit()
try:
	cur.close()
	conn.close()
except Exception as e:
	print(e)

