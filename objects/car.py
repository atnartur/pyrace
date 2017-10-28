from os import path
from pygame import *
from objects.base import Base

class Car(Base):
    COLOR__BLUE = 1
    COLOR__RED = 2

    def __init__(self, x, y, color=COLOR__BLUE):
        self.x = x
        self.y = y
        self.color = color

    def update(self, screen):
        img = image.load(path.join('files', 'car_%s.png' % self.color))
        screen.blit(img, (self.x - img.get_width() / 2, self.y - img.get_height() / 2))

    def render(self, screen):
        pass