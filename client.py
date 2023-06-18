import requests
import socket

class Client():
    
    def __int__(self):
        self.s_clnt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s_clnt.connect(('127.0.0.1', 1234))
        while True:

            self.s_clnt.send(bytes('main_data', 'utf-8'))
            msg = self.s_clnt.recv(1024)
            print(msg.decode('utf-8'))

    def get_request_data(self):
        return requests.get('main_data')

