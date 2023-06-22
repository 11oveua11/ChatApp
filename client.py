import socket
from config import *

class Client():
    
    def __int__(self):
        pass


    def get_request_data(self, *req_data):
        self.s_clnt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s_clnt.connect((conf['server'], conf['port']))
        req_key = req_data[0]
        match req_key:
            case 'new_user':
                self.s_clnt.send(bytes(' '.join(req_data), 'utf-8'))
                self.full_msg = ""
                while True:
                    msg = self.s_clnt.recv(1024)
                    if len(msg) <= 0:
                        break
                    self.full_msg += msg.decode('utf-8')
                return self.full_msg

            case 'test':
                self.s_clnt.send(bytes('test', 'utf-8'))
                self.full_msg = True
                while True and self.full_msg:
                    self.full_msg = self.s_clnt.recv(1024)
                return self.full_msg

            case _:
                return "неизвестный запрос"
