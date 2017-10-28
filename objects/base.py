from abc import *

class Base:
    @abstractmethod
    def update(self, screen):
        pass

    @abstractmethod
    def render(self, screen):
        pass