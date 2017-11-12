from pygame import *

from objects.base import Base
from objects.interface.text import Text
from settings import colors, name


class InfoPanel(Base):
    def __init__(self, offset_x=0):
        self.score = 0

        self.header_x = offset_x + 100
        self.score_x = offset_x + self.header_x + 260

        hotkey_x = self.score_x + 220
        hotkey_first_line = 17
        hotkey_second_line = hotkey_first_line + 17

        self.objects = [
            Text(name, offset=(self.header_x, 25), size=40, type=Text.TYPE__BOLD),
            Text('очков', offset=(self.score_x + 70, 25), size=30, type=Text.TYPE__BOLD),
            Text('<, >', offset=(offset_x + hotkey_x, hotkey_first_line), size=15, type=Text.TYPE__BOLD),
            Text('перемещение машинки', offset=(hotkey_x + 120, hotkey_first_line), size=15),
            Text('Q, ESC', offset=(offset_x + hotkey_x + 10, hotkey_second_line), size=15, type=Text.TYPE__BOLD),
            Text('выход', offset=(offset_x + hotkey_x + 63, hotkey_second_line), size=15)
        ]

    def update(self, screen):
        pass

    def render(self, screen):
        w, h = screen.get_size()
        draw.rect(screen, colors['blue'], (0, 0, w, 50))
        Text('%03d' % self.score, offset=(self.score_x, 25), size=41, type=Text.TYPE__DIGITAL).render(screen)
        draw.line(screen, (255, 255, 255), (self.score_x - 30, 0), (self.score_x - 30, 49))
        draw.line(screen, (255, 255, 255), (self.score_x + 117, 0), (self.score_x + 117, 49))
        [o.render(screen) for o in self.objects]