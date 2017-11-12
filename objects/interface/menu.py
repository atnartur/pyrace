from os import path

from pygame import *

from core.key_bindings import KeyBindings
from core.multiplayer_settings import MultiplayerSettings
from objects.base import Base
from objects.game.car import Car
from objects.interface.button import Button
from objects.interface.selector import Selector
from objects.interface.text import Text
from objects.simple import Simple
from settings import colors, name


class Menu(Base):
    GAME_TYPE__SINGLEPLAYER = 0
    GAME_TYPE__MULTIPLAYER = 1

    def __init__(self, screen, game):
        self.game = game
        self.screen = screen
        w, h = screen.get_size()

        first_line = 70
        img = image.load(path.join('files', 'images', 'car_%s.png' % Car.COLOR__BLUE))

        self.selector = Selector([
            Button("Один игрок", (w / 2, 200)),
            Button("Мультиплеер", (w / 2, 310)),
        ])

        self.objects = self.selector.buttons + [
            Text(name, offset=(w / 2 + 30, first_line), size=50, type=Text.TYPE__BOLD),
            Simple(update=lambda screen: screen.blit(img, (w / 2 - 100 - img.get_width() / 2, first_line - img.get_height() / 2))),

            Text("Используйте пробел и стрелки для", offset=(w / 2, 380), size=20),
            Text("навигации по меню", offset=(w / 2, 400), size=20),

            Text("Игровые горячие клавиши", offset=(w / 2, 440), size=20, type=Text.TYPE__BOLD),
            Text("Стрелка вверх - ускорение вперед", offset=(w / 2, 460), size=20),
            Text("Стрелки влево/вправо - управление машиной", offset=(w / 2, 480), size=20),
            Text("TAB - ускорение поворота машины", offset=(w / 2, 500), size=20),
            Text("Q, Esc - выход", offset=(w / 2, 520), size=20),

            Simple(lambda screen: draw.line(screen, colors['blue'], (0, 560), (screen.get_size()[0], 560), 2)),

            Text("© 2017 Булат Гиниятуллин, Артур Атнагулов", offset=(w / 2, 580), size=17),
        ]

        KeyBindings.register(K_SPACE, self.start)

    def clear_screen(self):
        self.objects = []

    def update(self, screen):
        [o.update(screen) for o in self.objects]

    def render(self, screen):
        [o.render(screen) for o in self.objects]

    def start(self):
        KeyBindings.deregister(K_SPACE)
        self.selector.close()
        self.clear_screen()

        if self.selector.active == Menu.GAME_TYPE__SINGLEPLAYER:
            self.game.start()
        else:
            MultiplayerSettings(self)
