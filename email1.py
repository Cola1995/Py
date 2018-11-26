#coding=utf-8
import smtplib
from email.mime.text import MIMEText
msg_from='991571566@qq.com'                                 #发送方邮箱
passwd='kvmgnchjqnuqbbji'                                   #填入发送方邮箱的授权码
msg_to='991571566@qq.com'                                  #收件人邮箱
                            
subject="测试报告"                                                 #主题     
content="车辆信息已查到"  #正文
msg = MIMEText(content)

file_new=r"C:\Users\Administrator\Desktop\Py\test_report\report2018_10_11_11_55_16.html"
f = open(file_new,'rb')
mail_body = f.read()
f.close()
msg = MIMEText(mail_body,'html','utf-8')
msg['Subject'] = subject
msg['From'] = msg_from
msg['To'] = msg_to


try:
    s = smtplib.SMTP_SSL("smtp.qq.com",465)      #邮件服务器及端口号
    s.login(msg_from, passwd)
    s.sendmail(msg_from, msg_to, msg.as_string())
    print ("发送成功")
except s.SMTPException.e:
    print ("发送失败")
finally:
    s.quit()
