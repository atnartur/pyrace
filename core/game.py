from core.player import Player
from core.remote_player import RemotePlayer
from multiplayer.client import Client
from multiplayer.remote import Remote
from multiplayer.server import Server

class Game:
    def __init__(self, objects):
        self.objects = objects
        self.player = Player(objects)

    def start(self):
        self.player.start()

    def multiplayer_start(self):
        Remote.events_init()
        self.start()
        self.remote_player = RemotePlayer(self.player.objects)
        self.remote_player.start()

    def create_server(self):
        self.server = Server()
        Remote.set_instance(self.server)

    def create_client(self, ip):
        self.client = Client(ip)
        Remote.set_instance(self.client)