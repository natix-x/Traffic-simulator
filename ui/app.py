import os

import pygame
from pygame.locals import *


# TODO: dodać ekran powitalny z możliwością wyboru configuracji przez użytkownika
# TODO: szybkość zmian, ilość pojawiających się samochodów, ilość skrzyżowań itp
class App:
    """Create a single-window app."""

    def __init__(self):
        """Initialize pygame and the application."""
        pygame.init()
        self.running = True
        self._initialize_display()
        # self.simulation_engine = SimulationEngine(traffic_system=)

    def _initialize_display(self):
        """Initialize and configure the main Pygame display."""
        # flags = RESIZABLE  # TODO: dostosować później zmiany w wielkości okna (trudnee)
        self.screen = pygame.display.set_mode((512, 512))
        self.background = pygame.transform.scale(
            pygame.image.load(os.path.join("ui", "resources", "images", "intersection.png")), (512, 512)
        )
        pygame.display.set_caption("Traffic simulation")

    def run(self):
        """Run the main event loop."""
        while self.running:
            self.screen.blit(self.background, (0, 0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
            pygame.display.update()
        pygame.quit()
