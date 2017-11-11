from objects.base import Base
from objects.interface.button import Button
from settings import colors

class Final(Base):
    def __init__(self, screen, score):
        w, h = screen.get_size()
        self.button = Button("Вы набрали %s очков" % score, (w / 2, h / 2), color=colors['red'])
    def update(self, screen):
        pass

    def render(self, screen):
        self.button.render(screen)

