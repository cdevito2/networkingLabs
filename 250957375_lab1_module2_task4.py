'''
Created on Oct. 6, 2019

@author: chris
'''
import smtplib


username = "networkin4436@gmail.com"
password = "networkingLab1"
rcpt = "manidimi123123@hotmail.com"
mailserver = "smtp.gmail.com"
serverPort = 587
msg = "\r\n ChrisDevito. "
#endmsg = "\r\n.\r\n"
addmsg = "250957375"
totalMsg = msg
submitMsg = msg+addmsg



connectSocket = smtplib.SMTP(mailserver,serverPort)#establish connection
connectSocket.ehlo()#helo command
connectSocket.starttls()#start TLS as needed by google
connectSocket.login(username, password)#send credentials
connectSocket.sendmail(username, rcpt, submitMsg)#send message to server
connectSocket.quit()#end connection
