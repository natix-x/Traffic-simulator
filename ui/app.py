import pygame
from pygame.locals import *
import os


class App:
    """Create a single-window app with multiple scenes."""

    def __init__(self):
        """Initialize pygame and the application."""
        pygame.init()
        flags = RESIZABLE
        self.screen = pygame.display.set_mode((640, 240), flags)
        self.background = pygame.image.load(os.path.join("resources", "images", "intersection.png"))
        self.running = True

    def run(self):
        """Run the main event loop."""
        while self.running:
            self.screen.blit(self.background, (0, 0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
            pygame.display.update()
        pygame.quit()


if __name__ == '__main__':
    App().run()
