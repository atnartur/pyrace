from pygame import *
from objects.base import Base
from objects.text import Text
from settings import colors

class Button(Base):
    def __init__(self, text, offset, is_active=False, color=colors['blue']):
        self.sizes = (600, 100)
        self.offset = offset
        self.is_active = is_active
        self.color = color
        x, y = offset
        self.text = Text(text, offset=(x, y), size=30, type=Text.TYPE__BOLD)

    def update(self, screen):
        pass

    def render(self, screen):
        x, y = self.offset
        x_size, y_size = self.sizes
        draw.rect(screen, self.color, (x - x_size / 2, y - y_size / 2, x_size, y_size))
        self.text.render(screen)
