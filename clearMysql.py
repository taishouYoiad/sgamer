import MySQLdb
import time

DAY_TO_SEC = 24 * 60 * 60

curr_time = int(time.time())
flag_time = curr_time - DAY_TO_SEC

try:
	conn = MySQLdb.connect(host = 'localhost', user = 'root', passwd = '123456', db = 'sgamer', port = 3306)
	cur = conn.cursor()
	sql = "delete from web where time<" + str(flag_time) + ""
	print(sql)
	res = cur.execute(sql)
	print(res)
	conn.commit()
	cur.close()
	conn.close()
	
except Exception as e:
	print(e) 
