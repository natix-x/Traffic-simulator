import pygame
from pygame.locals import *

from config import AppConfig
from ui.buttons.start_game_button import StartGameButton
from ui.presenters.simulation_screen import SimulationScreen


# TODO: dodać ekran powitalny z możliwością wyboru configuracji przez użytkownika
# TODO: szybkość zmian, ilość pojawiających się samochodów, ilość skrzyżowań itp
class App:
    def __init__(self):
        pygame.init()
        self.running = True
        self._initialize_display()
        self.intro_screen()

    def _initialize_display(self):
        # flags = RESIZABLE  # TODO: dostosować później zmiany w wielkości okna (trudnee)
        self.screen = pygame.display.set_mode((512, 512))
        pygame.display.set_caption("Welcome screen.")

    def intro_screen(self):
        start_button = StartGameButton(200, 200, 100, 50, AppConfig.WHITE, AppConfig.BLACK, 'Start', 32)
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if start_button.is_pressed(mouse_pos, mouse_pressed):
                self.running = False
                SimulationScreen(self.screen)

            start_button.draw(self.screen)
            pygame.display.update()
