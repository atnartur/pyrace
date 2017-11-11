from core.player import Player

class Game:
    def __init__(self, objects, with_remote=False):
        self.objects = objects
        self.player = Player(objects)

    def start(self):
        self.player.start()