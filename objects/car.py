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
        self.img = image.load(path.join('files', 'images', 'car_%s.png' % self.color))

    def update(self, screen):
        # print(img.get_width(), img.get_height())
        screen.blit(self.img, (self.x - self.img.get_width() / 2, self.y - self.img.get_height() / 2))

    def render(self, screen):
        pass