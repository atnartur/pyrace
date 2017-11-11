from pygame import *
from core.key_bindings import KeyBindings
from objects.interface.button import Button
from objects.interface.selector import Selector


class MultiplayerSettings:
    def __init__(self, menu):
        self.menu = menu
        self.step1()

    def step1(self):
        w = self.menu.screen.get_width()
        self.selector = Selector([
            Button("Запустить сервер", (w / 2, 240)),
            Button("Подключиться к серверу", (w / 2, 360)),
        ])
        self.menu.objects = self.selector.buttons

        KeyBindings.register(K_SPACE, lambda: lambda: self.step2(self.selector.active))

    def step2(self, active):
        self.selector.close()
        self.menu.objects = []

        if active == 0: # мы сервер
            pass
        else: # мы клиент
            pass

