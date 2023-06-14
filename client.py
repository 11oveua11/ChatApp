import requests

class Client():
    def __int__(self):
        self.req = '127.0.0.1:5000/main_data'
        # self.data = requests.get(self.req)
        # print(self.data)

    def get_request_data(self):
        return requests.get('main_data')
