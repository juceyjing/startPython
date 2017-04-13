#_*_ coding:UTF-8 _*_

import socket


s = socket.socket()
host = socket.gethostname()
port = 12345

s.connect((host,port))
print s.recv(1024)
s.close()


#客户端
#创建一个socket对象，取ip地址和端口号
#创建一个连接，调s.recv接收数据显示