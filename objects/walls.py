from pygame import *
from random import randint
from objects.base import Base

class Walls(Base):
    color = (128, 128, 128)

    def __init__(self, size, cube_size = 10, margin=0, offset=(0, 0)):
        self.pixels = []
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
        min_wall_width = 2  # минимальная ширина стены
        max_wall_width = int(w / 2)  # максимальная ширина стены
        x_count = w - self.margin * 2  # количество пикселей

        for y in range(0, h - self.margin * 2):
            is_need_wall = randint(1, is_need_wall_k)  # нужна ли стена на данной строчке
            arr = [0] * x_count

            if is_need_wall == 1:
                direction = randint(0, 1) == 0  # определяем сторону, в которую надо нарисовать стену
                count = randint(min_wall_width, max_wall_width)

                for i in range(0, count):
                    if direction:
                        arr[x_count - 1 - i] = 1
                    else:
                        arr[i] = 1

            self.pixels.append(arr)

    def update(self, screen):
        pass

    def render(self, screen):
        offset_x, offset_y = self.offset
        for y, arr in enumerate(self.pixels):
            for x, val in enumerate(arr):
                if val:
                    draw.rect(
                        screen,
                        Walls.color,
                        (
                            offset_x + (self.margin + x) * self.cube_size,
                            offset_y + (self.margin + y) * self.cube_size,
                            self.cube_size,
                            self.cube_size
                        )
                    )
