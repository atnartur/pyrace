import pygame, time
from core.key_bindings import KeyBindings
from app import providers

class Loop:
    def __init__(self, screen, objects):
        self.screen = screen
        self.objects = objects
        self.is_go = False

    def fill_black(self):
        self.screen.fill((0, 0, 0))

    def providers(self):
        [p(self.screen) for p in providers]

    def update(self):
        [o.update(self.screen) for o in self.objects]

    def render(self):
        [o.render(self.screen) for o in self.objects]
        pygame.display.flip()
        pygame.event.pump()

    def force_rerender(self):
        self.fill_black()
        self.providers()
        self.update()
        self.render()

    def run(self):
        self.is_go = True

        frames = 0
        t = time.time()

        while self.is_go:
            if time.time() - t > 1:
                print('FPS: %s' % frames)
                t = time.time()
                frames = 0

            self.force_rerender()

            frames += 1

            KeyBindings.exec(pygame.key.get_pressed())

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.stop()

        pygame.display.quit()

    def stop(self):
        self.is_go = False