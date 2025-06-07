import pygame
from pygame.locals import *

from simulation.config import AppConfig
from simulation.ui.buttons.custom_button import CustomButton
from simulation.ui.presenters.config_screen import ConfigScreen


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
        start_button = CustomButton(100, 200, 300, 50, AppConfig.WHITE, AppConfig.BLACK, 'Start', 20)

        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if start_button.is_pressed(mouse_pos, mouse_pressed):
                self.running = False
                ConfigScreen(self.screen)

            start_button.draw(self.screen)
            pygame.display.update()
