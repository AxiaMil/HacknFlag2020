#!/usr/bin/python3
import socket
import time
import hashlib
import socket

host = "ctf.nullsecsig.com"
port = 8081
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
print("Connected")
for _ in range(10):
	result = s.recv(1024).strip();
	print(result.decode())
	string = result[-20:]
	md5 = hashlib.md5(string.decode('utf-8').encode()).hexdigest().encode()
	s.send(md5 + "\n".encode())
	print('Send: ' + md5.decode())
