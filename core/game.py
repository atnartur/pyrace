from core.player import Player
from multiplayer.server import Server


class Game:
    def __init__(self, objects, with_remote=False):
        self.objects = objects
        self.player = Player(objects)

    def start(self):
        self.player.start()

    def create_server(self):
        self.server = Server()