# Client Program
import socket
HOST = 'localhost'
PORT = 50007
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))
s.send('Hello World!')
data = s.recv(1024)
s.close()
print 'Received', repr(data)
