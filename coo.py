import urllib
import urllib2
import cookielib

filename = "cookie.txt"

cookie = cookielib.MozillaCookieJar(filename)

#cookie = cookielib.CookieJar()
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
response = opener.open("http://www.baidu.com")
for item in cookie:
	print("Name  = " + item.name)
	print("Value = " + item.value)
cookie.save(ignore_discard = True, ignore_expires = True)

