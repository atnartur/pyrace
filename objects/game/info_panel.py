from pygame import *

from objects.base import Base
from objects.interface.text import Text
from settings import colors, name, width


class InfoPanel(Base):
    def __init__(self, offset_x=0):
        self.score = 0

        self.offset_x = offset_x
        self.header_x = offset_x + 100
        self.score_x = self.header_x + 260

        self.objects = [
            Text(name, offset=(self.header_x, 25), size=40, type=Text.TYPE__BOLD),
            Text('очков', offset=(self.score_x + 75, 25), size=30, type=Text.TYPE__BOLD)
        ]

    def update(self, screen):
        pass

    def render(self, screen):
        draw.rect(screen, colors['blue'], (self.offset_x, 0, width, 50))
        Text('%03d' % self.score, offset=(self.score_x, 25), size=41, type=Text.TYPE__DIGITAL).render(screen)
        [o.render(screen) for o in self.objects]