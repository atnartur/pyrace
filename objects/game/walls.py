from random import randint

from pygame import *

import time

from core.events import Events
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
        self.max_wall_width = 3 * int(size[0]/cube_size / 5)  # максимальная ширина стены
        self.top_margin = 50
        self.speed = 1
        self.is_accelerated = False
        self.acceleration_start_time = 0
        self.is_acceleration_started = False
        self.acceleration_coefficient = 1
        self.removed_walls = 0
        self.wall_generated_callback = None
        self.is_stopped = False
        Events.last_wall = self.get_last_wall()

    def generate_wall(self, top_margin):
        direction = randint(0, 1) == 0
        width = randint(self.min_wall_width, self.max_wall_width)
        wall = (top_margin, width * self.cube_size, direction)
        self.coordinates.append(wall)
        if self.wall_generated_callback is not None:
            self.wall_generated_callback(wall)

    def generate(self):
        w, h = self.size

        w = int(w / self.cube_size)
        h = int(h / self.cube_size)

        y = self.top_margin / self.cube_size
        while y <= h - 2 * self.margin/self.cube_size:
            self.generate_wall(y * self.cube_size)
            y += self.margin/self.cube_size

    def update(self, screen):
        if self.is_stopped or len(self.coordinates) == 0:
            return

        if self.is_accelerated and not self.is_acceleration_started:
            self.speed *= self.acceleration_coefficient
            self.is_acceleration_started = True
            self.acceleration_start_time = time.time()
        acc_timeout = Events.instance.acceleration_timeout
        if self.is_accelerated and time.time() - self.acceleration_start_time >= acc_timeout:
            self.speed //= self.acceleration_coefficient
            self.is_accelerated = False
            self.is_acceleration_started = False
        w, h = self.size
        for i in range(len(self.coordinates)):
            y, width, direction = self.coordinates[i]
            self.coordinates[i] = (y + self.speed, width, direction)
        if min(self.coordinates, key=lambda x: x[0])[0] - self.top_margin >= self.margin:
            self.generate_wall(self.top_margin)

        last_wall = self.get_last_wall()
        if last_wall is not None and last_wall[0] >= h:
            self.coordinates.remove(last_wall)
            self.removed_walls += 1

    def get_last_wall(self):
        if len(self.coordinates) > 0:
            return self.coordinates[0]
        else:
            return None

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

    def stop(self):
        self.is_stopped = True
