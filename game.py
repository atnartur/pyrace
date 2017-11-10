import pygame

from core.key_bindings import KeyBindings
from objects.car import Car
from objects.walls import Walls
from objects.info_panel import InfoPanel
from settings import *
from core.events import Events
from app import providers


class Game:
    def __init__(self, objects):
        self.objects = objects

    def start(self):
        car = Car(width / 2, height - 60)
        self.objects.append(car)
        self.objects.append(InfoPanel())
        walls = Walls((width, height), margin=1.5 * car.img.get_height())
        self.objects.append(walls)
        Events.instance = Events(car, walls)

        KeyBindings.register(pygame.K_LEFT, Events.instance.shift_left)
        KeyBindings.register(pygame.K_RIGHT, Events.instance.shift_right)
        KeyBindings.register(pygame.K_UP, lambda: Events.instance.accelerate(2))
        providers.append(self.provider_handler)
        KeyBindings.register(pygame.K_TAB, lambda: Events.instance.accelerate_car(2))

    def provider_handler(self, screen):
        if Events.instance.is_collision():
            print("BUMP!")
