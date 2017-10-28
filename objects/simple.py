from objects.base import Base

class Simple(Base):
    def __init__(self, render=lambda screen: None, update=lambda screen: None):
        self.update = update
        self.render = render