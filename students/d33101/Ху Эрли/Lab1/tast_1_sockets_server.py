# -*- coding:utf-8 -*-
"""
作者:酷酷酷
日期:2021年09月21日
"""
import socket

server = socket.socket()
host = '127.0.0.1'
port = 5555
server.bind((host, port))
server.listen(1)

conn, addr = server.accept()
data = conn.recv(1024)
udata = data.decode('utf-8')
print(udata)
conn.send(b"Hello, client! \n")
conn.close()