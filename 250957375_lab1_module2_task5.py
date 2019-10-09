'''
Created on Oct. 6, 2019

@author: chris
'''
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

import os

username = "networkin4436@gmail.com"
password = "networkingLab1"
rcpt = "manidimi123123@hotmail.com"
mailserver = "smtp.gmail.com"
serverPort = 587
msg = "\r\n ChrisDevito. "
#endmsg = "\r\n.\r\n"
addmsg = "250957375"

submitMsg = msg+addmsg

msg = MIMEMultipart()
msg['From'] = username
msg['To'] = rcpt
msg_content = MIMEText(submitMsg, 'plain', 'utf-8')
msg.attach(msg_content)

img_data = open("space.jpg", 'rb').read()
image = MIMEImage(img_data, name=os.path.basename("space.jpg"))
msg.attach(image)

connectSocket = smtplib.SMTP(mailserver,serverPort)#establish connection
connectSocket.ehlo()#send helo command
connectSocket.starttls()#start tls as required by google
connectSocket.login(username, password)#send login credentials
connectSocket.sendmail(username, rcpt, msg.as_string())#send message to recipient
connectSocket.quit()#end connection to server