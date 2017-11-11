from pygame import *
import time
from core.key_bindings import KeyBindings
from objects.base import Base

class Selector(Base):
    def __init__(self, buttons):
        self.buttons = buttons
        self.active = 0
        self.update_active()
        self.t = time.time()

        KeyBindings.register(K_UP, self.key_handler(lambda: self.up()))
        KeyBindings.register(K_DOWN, self.key_handler(lambda: self.down()))

    def up(self):
        if self.active > 0:
            self.active -= 1
            self.update_active()

    def down(self):
        if self.active < len(self.buttons) - 1:
            self.active += 1
            self.update_active()

    def key_handler(self, action):
        def handler():
            if time.time() - self.t > 0.01:
                action()
                self.t = time.time()
        return handler

    def update(self, screen):
        pass

    def render(self, screen):
        [o.render(screen) for o in self.buttons]

    def update_active(self):
        for arr_index, button in enumerate(self.buttons):
            if arr_index == self.active:
                button.is_active = True
            else:
                button.is_active = False

    def set_active(self, active):
        self.active = active
        self.update_active()

    def close(self):
        KeyBindings.deregister(K_UP)
        KeyBindings.deregister(K_DOWN)