import pygame

pygame.display.init()
pygame.display.set_caption('PyRace')

width = 800
height = 600
screen = pygame.display.set_mode((width, height))

objects = []

if __name__ == '__main__':
    from core.loop import Loop

    loop = Loop(screen, objects)
    loop.run()