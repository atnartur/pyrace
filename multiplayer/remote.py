import json
from settings import server_packet_size

class Remote:
    """
    Логика общения с удаленным устройством
    """

    def __init__(self, remote_instance):
        self.remote = remote_instance

    def send_start(self):
        self.send('start')

    def send(self, command, data = None):
        self.remote.sender.sendall(json.dumps({
            'command': command,
            'data': data
        }).encode())

    def receive(self):
        return json.loads(self.remote.sender.recv(server_packet_size).decode())