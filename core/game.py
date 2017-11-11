from core.player import Player

class Game:
    def __init__(self, objects, count_of_players=1):
        self.objects = objects
        self.player = Player(objects)

    def start(self):
        self.player.start()