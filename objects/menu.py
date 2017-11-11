from pygame import *
from os import path
from objects.base import Base
from objects.car import Car
from objects.text import Text
from objects.simple import Simple
from objects.button import Button
from settings import colors, name
from core.key_bindings import KeyBindings

class Menu(Base):
    def __init__(self, screen, game):
        w, h = screen.get_size()

        first_line = 100
        img = image.load(path.join('files', 'images', 'car_%s.png' % Car.COLOR__BLUE))
        self.objects = [
            Text(name, offset=(w / 2 + 30, first_line), size=50, type=Text.TYPE__BOLD),

            Button("Нажмите ПРОБЕЛ, чтобы начать игру", (w / 2, 300)),

            Text("Горячие клавиши", offset=(w / 2, 450), size=20, type=Text.TYPE__BOLD),
            Text("Q, Esc - выход", offset=(w / 2, 480), size=20),

            Simple(update=lambda screen: screen.blit(img, (w / 2 - 100 - img.get_width() / 2, first_line - img.get_height() / 2))),

            Simple(lambda screen: draw.line(screen, colors['blue'], (0, 560), (screen.get_size()[0], 560), 2)),

            Text("© 2017 Булат Гиниятуллин, Артур Атнагулов", offset=(w / 2, 580), size=17),
        ]

        def start():
            print('start')
            self.objects = []
            KeyBindings.deregister(K_SPACE)
            game.start()

        KeyBindings.register(K_SPACE, start)

    def update(self, screen):
        [o.update(screen) for o in self.objects]

    def render(self, screen):
        [o.render(screen) for o in self.objects]



