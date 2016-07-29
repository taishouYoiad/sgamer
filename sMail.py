# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'xx@sgamer.com'
receivers = ['zhukai01@qq.com']

content = "Sgamer Test !"

message = MIMEText(content, 'plain', 'utf-8')
message['From'] = Header("Sgamer", 'utf-8')
message['To'] =  Header("kzhu", 'utf-8')

subject = 'Sgamer 自动刷选'
message['Subject'] = Header(subject, 'utf-8')


try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, message.as_string())
    print "邮件发送成功"
except smtplib.SMTPException:
    print "Error: 无法发送邮件"
