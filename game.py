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
        self.car = Car(width / 2, height - 60)
        self.walls = Walls((width, height), margin=1.5 * self.car.img.get_height())
        self.info_panel = InfoPanel()

        self.objects.append(self.car)
        self.objects.append(self.walls)
        self.objects.append(self.info_panel)

        Events.instance = Events(self.car, self.walls)

        KeyBindings.register(pygame.K_LEFT, Events.instance.shift_left)
        KeyBindings.register(pygame.K_RIGHT, Events.instance.shift_right)
        KeyBindings.register(pygame.K_UP, lambda: Events.instance.accelerate(2))
        KeyBindings.register(pygame.K_TAB, lambda: Events.instance.accelerate_car(5))

        providers.append(self.provider_handler)
        self.previous_last_wall = None

    def provider_handler(self, screen):
        if Events.instance.is_collision():
            pass

        last_wall = self.walls.get_last_wall()

        if last_wall is not None and self.car.y < last_wall[0] and self.walls.removed_walls == self.info_panel.score:
            self.info_panel.score += 1
            self.previous_last_wall = last_wall