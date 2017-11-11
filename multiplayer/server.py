import socket, json
from settings import server_port, server_packet_size

class Server:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind(('', server_port))
        self.s.listen(2)
        self.msg_size = server_packet_size

    def get_machine_ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip

    def get_msg(self, conn):
        return json.load(conn.recv(self.msg_size).decode())

    def waiting_for_connect(self):
        conn, addr = self.s.accept()
        cmd = self.get_msg(conn)
        print(conn, addr, cmd)
