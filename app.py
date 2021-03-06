import pygame

from settings import *

objects = []
providers = [] # глобальные обработчики события отрисовки. Такие обработчики не привязаны к объектам
events_handlers = [] # обрботчики событий pygame

if __name__ == '__main__':
    from core.loop import Loop
    from core.key_bindings import KeyBindings
    from objects.interface.menu import Menu
    from core.game import Game

    pygame.display.init()
    pygame.display.set_caption(name)

    screen = pygame.display.set_mode((width, height))

    pygame.font.init()
    game = Game(objects)

    objects.append(Menu(screen, game))

    loop = Loop(screen, objects)
    game.loop = loop

    KeyBindings.register(pygame.K_ESCAPE, lambda: loop.stop())
    KeyBindings.register(pygame.K_q, lambda: loop.stop())

    loop.run()