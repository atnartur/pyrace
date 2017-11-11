import socket, json
from settings import server_port

class Client:
    def __init__(self, host):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((host, server_port))

    def send_start(self):
        self.send('start')

    def send(self, command, data = None):
        self.s.sendall(json.dumps({
            'command': command,
            'data': data
        }).encode())