from objects.car import Car
from objects.walls import Walls
from settings import *

class Game:
    def __init__(self, objects):
        self.objects = objects

    def start(self):
        self.objects.append(Car(width / 2 - 100, height / 2))
        self.objects.append(Car(width / 2 + 100, height / 2, Car.COLOR__RED))
        self.objects.append(Walls((width, height - 50)))