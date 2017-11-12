import json, socket, errno
from settings import server_packet_size
from app import providers
from json.decoder import JSONDecodeError
from multiplayer.sender import Sender
from multiplayer.receiver import Receiver

class Remote:
    """
    Логика общения с удаленным устройством
    """

    instance = None
    sender = None
    receiver = None

    @staticmethod
    def set_instance(instance):
        Remote.instance = instance

    @staticmethod
    def events_init():
        print('remote events start')
        Remote.instance.sender.setblocking(0)
        providers.append(Remote.provider)

    @staticmethod
    def stop():
        providers.remove(Remote.provider)

    @staticmethod
    def send(command, data = None):
        if Remote.instance is not None:
            packet = {
                'command': command,
                'data': data
            }
            print('socket send', packet)
            Remote.instance.sender.sendall(json.dumps(packet).encode())

    @staticmethod
    def receive():
        if Remote.instance is None:
            return None
        res = Remote.instance.sender.recv(server_packet_size).decode()
        try:
            packet = json.loads(res)
            print('socket received', packet)
            return packet
        except JSONDecodeError:
            return None

    @staticmethod
    def provider(screen):
        try:
            msg = Remote.receive()
        except socket.error as e:
            err = e.args[0]
            if err != errno.EAGAIN and err != errno.EWOULDBLOCK: # a "real" error occurred
                print('socket error', e)
        else:
            print(msg)

Remote.sender = Sender(Remote)
Remote.receiver = Receiver(Remote)