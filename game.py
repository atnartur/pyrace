from objects.car import Car
from objects.walls import Walls
from objects.info_panel import InfoPanel
from settings import *

class Game:
    def __init__(self, objects):
        self.objects = objects

    def start(self):
        car = Car(width / 2, height - 60)
        self.objects.append(car)
        self.objects.append(Walls((width, height), margin=1.5 * car.img.get_height()))
        self.objects.append(InfoPanel())
