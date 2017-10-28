import pygame, time
from core.key_bindings import KeyBindings

class Loop:
    def __init__(self, screen, objects):
        self.screen = screen
        self.objects = objects
        self.is_go = False

    def run(self):
        self.is_go = True

        frames = 0
        t = time.time()

        while self.is_go:
            if time.time() - t > 1:
                print('FPS: %s' % frames)
                t = time.time()
                frames = 0

            self.screen.fill((0, 0, 0))

            [o.update(self.screen) for o in self.objects]

            frames += 1

            self.screen.lock()
            [o.render(self.screen) for o in self.objects]
            self.screen.unlock()

            pygame.display.flip()

            pygame.event.pump()
            KeyBindings.exec(pygame.key.get_pressed())

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.stop()

        pygame.display.quit()

    def stop(self):
        self.is_go = False