from flask import Flask
import socket

server = socket.create_server(('127.0.0.1', 5000))
server.listen(100)
client_socket, adress = server.accept()
data = client_socket.recv(1024).decode('utf-8')
print(data)
content = 'well done!!!!!!!!'.encode('utf-8')
client_socket.send(content)
print('shut....')
