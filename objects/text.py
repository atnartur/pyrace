from pygame import *
from objects.base import Base

class Text(Base):
    TYPE__BOLD = 'files/fonts/Roboto-Bold.ttf'
    TYPE__REGULAR = 'files/fonts/Roboto-Regular.ttf'
    TYPE__DIGITAL = 'files/fonts/digital.ttf'

    def __init__(self, text, offset=(0, 0), color=(255, 255, 255), type=TYPE__REGULAR, size=20):
        self.text = text
        self.color = color
        self.offset = offset
        self.font = font.Font(type, size)

    def update(self, screen):
        text = self.font.render(self.text, True, self.color)
        # print(self.text, text.get_width(), text.get_height())

        x, y = self.offset
        x -= text.get_width() / 2
        y -= text.get_height() / 2

        screen.blit(text, (x, y))

    def render(self, screen):
        pass