'''
Created on Oct. 6, 2019

@author: chris
'''
from socket import *
import base64
import ssl
msg = "\r\n ChrisDevito. 250957375"
endmsg = "\r\n.\r\n"
addmsg = "250957375"

#submitMsg = msg+addmsg
# Choose a mail server (e.g. Google mail server) and call it mailserver mailserver = #Fill in start #Fill in end
mailserver = "smtp.gmail.com"#i chose google for my mail server
serverPort = 587;#google said to use either port 465 or 587, i chose 587 so i can use tls authentication

# Create socket called clientSocket and establish a TCP connection with mailserver


#Fill in start
clientSocket = socket(AF_INET,SOCK_STREAM)
#sock_stream indicates TCP socket rather than UDP
#AF_INET indicates network is using ipv4
#just creating socket called clientSocket
print("gonna connect")#output statment
clientSocket.connect((mailserver,serverPort))#establishing TCP connection
print("connected")
#handshake is performed, connection established


#Fill in end
recv = clientSocket.recv(1024).decode() #getting server response
print(recv)#outputting server response
print("that was recv")
if recv[:3] != '220': #220 is good response so i want to know if a bad response occurs
    print('220 reply not received from server.')

# Send HELO command and print server response. 
helo = 'HELO Alice\r\n' 
clientSocket.send(helo.encode('utf-8')) #must encode the string to utf-8 to be accepted by google
resp = clientSocket.recv(1024).decode()  #get server response
print("helo: "+resp)
if resp[:3] != '250':
    print('heloCommand: 250 reply not received from server.')

tlsCommand = "STARTTLS\r\n" #gmail uses TLS security so i had to include this
clientSocket.send(tlsCommand.encode('utf-8')) #encode to utf-8 because thats what google requires
resp = clientSocket.recv(1024).decode()
print("tls: "+resp) # get TLS response and output
if resp[:3] != '220':
    print('startTls: 220 reply not received from server.')

Client_Socket_WrappedSSL = ssl.wrap_socket(clientSocket)
command = "AUTH LOGIN\r\n" #google requires socket to be wrapped with SSL
Client_Socket_WrappedSSL.send(command.encode('utf-8'))
resp = Client_Socket_WrappedSSL.recv(1024).decode()
print("authentication: "+resp)
if resp[:3] != '334':
    print('authlogon: 334 reply not received from server.')

username = input('Enter your username(include@gmail): ') #input full email
username = username.encode('utf-8') 
Client_Socket_WrappedSSL.send(base64.b64encode(username) + '\r\n'.encode('utf-8'))
resp = Client_Socket_WrappedSSL.recv(1024).decode()#gmail requires utf and base64 encoding
print("username: "+resp)
if resp[:3] != '334':
    print('sendusername: 334 reply not received from server.')

password = input ('Enter your password: ') #user enters password
password = password.encode('utf-8')
Client_Socket_WrappedSSL.send(base64.b64encode(password) + '\r\n'.encode('utf-8'))
resp = Client_Socket_WrappedSSL.recv(1024).decode()
print("psword: "+resp)#receive and output response
if resp[:3] != '235':
    print('sendpassword: 235 reply not received from server.')
print("email logon sent to server!")
# Send MAIL FROM command and print server response.
 
# Fill in start
mail = "MAIL FROM: <" + username.decode() + ">\r\n"
Client_Socket_WrappedSSL.send(mail.encode())
resp = Client_Socket_WrappedSSL.recv(1024).decode() 
print("mail resp: "+resp)
if resp[:3] != '250':
    print('MAILFROM COMMAND: 250 reply not received from server.')
# Fill in end

# Send RCPT TO command and print server response.

# Fill in start
rcpt = "manidimi123123@hotmail.com"
recipientTo = "RCPT TO: <" + rcpt + ">\r\n"
Client_Socket_WrappedSSL.send(recipientTo.encode());
resp = Client_Socket_WrappedSSL.recv(1024).decode() 
print("rcpt resp: "+resp)
if resp[:3] != '250':
    print('RCPT TO COMMAND: 250 reply not received from server.')
# Fill in end

# Send DATA command and print server response.

# Fill in start
dataMsg = "DATA\r\n"
Client_Socket_WrappedSSL.send(dataMsg.encode())#send data command and receive resp
resp = Client_Socket_WrappedSSL.recv(1024).decode() 
print(resp)
print("datacommand ^")
# Fill in end

# Send message data.

# Fill in start
Client_Socket_WrappedSSL.send(msg.encode()) #send the message to server
# Fill in end

# Message ends with a single period.

# Fill in start
endmsg = "\r\n.\r\n"
Client_Socket_WrappedSSL.send(endmsg.encode())#send end period
respEndMsg = Client_Socket_WrappedSSL.recv(1024).decode() 
print("end with period")
print("period resp: "+respEndMsg) # receive and output response
# Fill in end

# Send QUIT command and get server response.

# Fill in start
command = "QUIT\r\n"
Client_Socket_WrappedSSL.send(command.encode())#send quit command and receive response
resp = Client_Socket_WrappedSSL.recv(1024).decode() 
print("quit resp: "+resp)
if resp[:3] != '221':
    print('QUIT COMMAND: 221 reply not received from server.')
Client_Socket_WrappedSSL.close()
# Fill in end