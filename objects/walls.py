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
        self.min_wall_width = int(size[0]/cube_size / 4)  # минимальная ширина стены
        self.max_wall_width = 3 * int(size[0]/cube_size / 4)  # максимальная ширина стены
        self.top_margin = 50
        self.generate()

    def generate_wall(self, top_margin):
        direction = randint(0, 1) == 0
        width = randint(self.min_wall_width, self.max_wall_width)
        self.coordinates.append((top_margin, width * self.cube_size, direction))

    def generate(self):
        w, h = self.size

        w = int(w / self.cube_size)
        h = int(h / self.cube_size)

        y = self.top_margin / self.cube_size
        while y <= h - 2 * self.margin/self.cube_size:
            self.generate_wall(y * self.cube_size)
            y += self.margin/self.cube_size

    def update(self, screen):
        w, h = self.size
        for i in range(len(self.coordinates)):
            y, width, direction = self.coordinates[i]
            self.coordinates[i] = (y + 1, width, direction)

        if min(self.coordinates, key=lambda x: x[0])[0] - self.top_margin >= self.margin:
            self.generate_wall(self.top_margin)

        last_wall = max(self.coordinates, key=lambda x: x[0])

        if last_wall[0] >= h:
            self.coordinates.remove(last_wall)

    def render(self, screen):
        offset_x, offset_y = self.offset
        w, h = self.size
        for coordinate in self.coordinates:
            y, width, direction = coordinate
            if direction:
                x = offset_x
            else:
                x = offset_x + w - width
            draw.rect(screen, self.color, (x, offset_y + y, width, self.cube_size))
