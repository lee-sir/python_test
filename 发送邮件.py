#邮件发送方（发送地址，qq发送客户端授权密码xncacefklmvzicea，SMTP服务器地址smtp.qq.com）
#邮件内容
#邮件接收方
import smtplib
from email.mime.text import MIMEText

msg_from="1097689375@qq.com" #发送方
pwd = "qivulmuxjkwghcda"  # 授权码
to ="lixuegang@flashexpress.com"	

subject="这是Python发送的邮件！"
content="你家着火了！！"

#构造邮件
msg=MIMEText(content) #msg邮件对象(content,"html","utf-8")
msg["Subject"]=subject
msg["From"]=msg_from
msg["To"]=to

#发送邮件
ss=smtplib.SMTP_SSL("smtp.qq.com",465)
ss.login(msg_from,pwd)
ss.sendmail(msg_from,to,msg.as_string()) #发送