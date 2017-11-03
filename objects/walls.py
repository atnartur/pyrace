from pygame import *
from random import randint
from objects.base import Base


class Walls(Base):
    color = (128, 128, 128)

    def __init__(self, size, margin, cube_size=10, offset=(0, 0)):
        self.coordinates = []
        self.size = size
        self.cube_size = cube_size
        self.margin = margin
        self.offset = offset
        self.generate()

    def generate(self):
        w, h = self.size

        w = int(w / self.cube_size)
        h = int(h / self.cube_size)

        is_need_wall_k = 5  # вероятность создания стены - 1 к X
        min_wall_width = int(w / 4)  # минимальная ширина стены
        max_wall_width = 3 * int(w / 4)  # максимальная ширина стены

        y = 0
        while y <= h - 2 * self.margin/self.cube_size:
            was_created = False
            # is_need_wall = randint(1, is_need_wall_k) == 1
            if True:
                direction = randint(0, 1) == 0
                width = randint(min_wall_width, max_wall_width)
                self.coordinates.append((y*self.cube_size, width*self.cube_size, direction))
                was_created = True
            if was_created:
                y += self.margin/self.cube_size
            else:
                y += 1

    def update(self, screen):
        pass

    def render(self, screen):
        offset_x, offset_y = self.offset
        w, h = self.size
        for coordinate in self.coordinates:
            y, width, direction = coordinate
            if direction:
                x = offset_x
            else:
                x = offset_x + w - width
            draw.rect(screen, self.color,
                      (x, offset_y + y, width, self.cube_size))
