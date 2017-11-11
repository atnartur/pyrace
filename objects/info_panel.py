from pygame import *
from objects.base import Base
from settings import colors, name
from objects.text import Text

class InfoPanel(Base):
    def __init__(self):
        self.score = 0

        self.header_x = 100
        self.score_x = self.header_x + 260

        hotkey_x = self.score_x + 220
        hotkey_first_line = 17
        hotkey_second_line = hotkey_first_line + 17

        self.objects = [
            Text(name, offset=(self.header_x, 25), size=40, type=Text.TYPE__BOLD),
            Text('очков', offset=(self.score_x + 70, 25), size=30, type=Text.TYPE__BOLD),
            Text('<, >', offset=(hotkey_x, hotkey_first_line), size=15, type=Text.TYPE__BOLD),
            Text('перемещение машинки', offset=(hotkey_x + 120, hotkey_first_line), size=15),
            Text('Q, ESC', offset=(hotkey_x + 10, hotkey_second_line), size=15, type=Text.TYPE__BOLD),
            Text('выход', offset=(hotkey_x + 63, hotkey_second_line), size=15)
        ]

    def update(self, screen):
        w, h = screen.get_size()
        draw.rect(screen, colors['blue'], (0, 0, w, 50))
        Text('%03d' % self.score, offset=(self.score_x, 25), size=41, type=Text.TYPE__DIGITAL).update(screen)
        draw.line(screen, (255, 255, 255), (self.score_x - 30, 0), (self.score_x - 30, 49))
        draw.line(screen, (255, 255, 255), (self.score_x + 117, 0), (self.score_x + 117, 49))
        [o.update(screen) for o in self.objects]

    def render(self, screen):
        pass