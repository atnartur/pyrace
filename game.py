import pygame

from core.key_bindings import KeyBindings
from objects.car import Car
from objects.walls import Walls
from settings import *
from core.events import Events


class Game:
    def __init__(self, objects):
        self.objects = objects

    def start(self):
        car = Car(width / 2, height - 60)
        self.objects.append(car)
        walls = Walls((width, height), margin=1.5 * car.img.get_height())
        self.objects.append(walls)
        Events.instance = Events(car, walls)

        KeyBindings.register(pygame.K_LEFT, Events.instance.shift_left)
        KeyBindings.register(pygame.K_RIGHT, Events.instance.shift_right)
        KeyBindings.register(pygame.K_UP, lambda: Events.instance.accelerate(2))
