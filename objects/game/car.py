from os import path

from pygame import *

import time

from core.events import Direction, Events
from objects.base import Base


class Car(Base):
    COLOR__BLUE = 1
    COLOR__RED = 2

    def __init__(self, x, y, color=COLOR__BLUE):
        self.x = x
        self.y = y
        self.color = color
        self.img = image.load(path.join('files', 'images', 'car_%s.png' % self.color))
        self.direction = Direction.STRAIGHT
        self.is_accelerated = False
        self.acceleration_start_time = 0
        self.is_acceleration_started = False
        self.acceleration_coefficient = 1
        self.speed = 2
        self.is_stopped = False
        self.acc_stop_callback = None # колбек, который вызывается после остановки ускорения

    def update(self, screen):
        if self.is_stopped:
            return

        if self.is_accelerated and not self.is_acceleration_started:
            self.speed *= self.acceleration_coefficient
            self.is_acceleration_started = True
            self.acceleration_start_time = time.time()
        acc_timeout = Events.acceleration_timeout
        if self.is_accelerated and time.time() - self.acceleration_start_time >= acc_timeout:
            self.speed //= self.acceleration_coefficient
            self.is_accelerated = False
            self.is_acceleration_started = False
            if self.acc_stop_callback is not None:
                self.acc_stop_callback()
        if self.direction == Direction.LEFT:
            self.x -= self.speed
            self.direction = Direction.STRAIGHT
        elif self.direction == Direction.RIGHT:
            self.x += self.speed
            self.direction = Direction.STRAIGHT

    def render(self, screen):
        screen.blit(self.img, (self.x - self.img.get_width() / 2, self.y - self.img.get_height() / 2))

    def stop(self):
        self.is_stopped = True