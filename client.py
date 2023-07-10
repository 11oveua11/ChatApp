import socket
from config import *


class Client():

    def __int__(self):
        pass

    def get_request_data(self, *req_data, **kwargs):
        self.s_clnt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s_clnt.settimeout(0.5)
        try:
            self.s_clnt.connect((kwargs['server'], int(kwargs['port'])))
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
                    self.full_msg = ""
                    while True:
                        msg = self.s_clnt.recv(1024)
                        if len(msg) <= 0:
                            break
                        self.full_msg += msg.decode('utf-8')
                    return self.full_msg

                case _:
                    return "неизвестный запрос"
        except:
            return ('connect_false')
