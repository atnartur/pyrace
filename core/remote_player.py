from objects.game.car import Car
from objects.game.info_panel import InfoPanel
from objects.game.walls import Walls
from settings import *

class RemotePlayer:
    def __init__(self, objects):
        self.objects = objects

    def start(self):
        offset_x = width
        self.car = Car(offset_x + width / 2, height - 60)
        self.walls = Walls((width, height), margin=1.5 * self.car.img.get_height(), offset=(offset_x, 0))
        self.info_panel = InfoPanel(offset_x)

        self.objects.append(self.car)
        self.objects.append(self.walls)
        self.objects.append(self.info_panel)