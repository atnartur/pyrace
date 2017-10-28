from pygame import *
from objects.base import Base
from objects.car import Car
from objects.text import Text
from objects.simple import Simple

class Menu(Base):
    def __init__(self, screen):
        w, h = screen.get_size()

        first_line = 100
        self.objects = [
            Car(w / 2 - 100, first_line),
            Text("PyGame", offset=(w / 2 + 30, first_line), size=50, type=Text.TYPE__BOLD),
            Simple(lambda screen: draw.line(screen, (0, 153, 254), (0, 560), (screen.get_size()[0], 560), 2)),
            Text("© 2017 Булат Гиниятуллин, Артур Атнагулов", offset=(w / 2, 580), size=17),
        ]
        pass

    def update(self, screen):
        [o.update(screen) for o in self.objects]

    def render(self, screen):
        [o.render(screen) for o in self.objects]



