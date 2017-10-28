import pygame

pygame.display.init()
pygame.display.set_caption('PyRace')

width = 800
height = 600
screen = pygame.display.set_mode((width, height))

objects = []

if __name__ == '__main__':
    from core.loop import Loop
    from core.key_bindings import KeyBindings
    from objects.car import Car
    from objects.walls import Walls

    objects.append(Car(width / 2 - 100, height / 2))
    objects.append(Car(width / 2 + 100, height / 2, Car.COLOR__RED))
    objects.append(Walls((width, height - 50)))

    loop = Loop(screen, objects)

    KeyBindings.register(pygame.K_ESCAPE, lambda: loop.stop())
    KeyBindings.register(pygame.K_q, lambda: loop.stop())

    loop.run()