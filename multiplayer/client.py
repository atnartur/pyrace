import socket
from settings import server_port

class Client:
    def __init__(self, host):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((host, server_port))
        self.sender = self.s
        print('client connected')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('client close')
        self.s.close()
