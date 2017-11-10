import pygame
from settings import *

objects = []
providers = [] # глобальные обработчики события отрисовки. Такие обработчики не привязаны к объектам

if __name__ == '__main__':
    from core.loop import Loop
    from core.key_bindings import KeyBindings
    from objects.menu import Menu
    from game import Game

    pygame.display.init()
    pygame.display.set_caption('PyRace')

    screen = pygame.display.set_mode((width, height))

    pygame.font.init()
    game = Game(objects)

    objects.append(Menu(screen, game))

    loop = Loop(screen, objects)

    KeyBindings.register(pygame.K_ESCAPE, lambda: loop.stop())
    KeyBindings.register(pygame.K_q, lambda: loop.stop())

    loop.run()