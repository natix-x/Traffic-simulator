import os

import pygame
from pygame.locals import *

from ui.buttons.start_game_button import StartGameButton
from config import AppConfig


# TODO: dodać ekran powitalny z możliwością wyboru configuracji przez użytkownika
# TODO: szybkość zmian, ilość pojawiających się samochodów, ilość skrzyżowań itp
# TODO: Refaktoryzacja kodu, przenisienie części Symulacyjnego i SimulationPresenter
class App:
    def __init__(self):
        pygame.init()
        self.running = True
        self.background = pygame.transform.scale(
            pygame.image.load(os.path.join("ui", "resources", "images", "intersection.png")), (512, 512)
        )
        self._initialize_display()

    def _start_simulation(self):
        pygame.display.set_caption("Simulation")
        while self.running:
            self.screen.blit(self.background, (0, 0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
            pygame.display.update()
        pygame.quit()

        # simulation_engine = SimulationEngine(TrafficSystem(), self.screen)  # jeśli wymaga ekranu
        # uruchumoenie symulacji

    def _initialize_display(self):
        # flags = RESIZABLE  # TODO: dostosować później zmiany w wielkości okna (trudnee)
        self.screen = pygame.display.set_mode((512, 512))
        pygame.display.set_caption("Welcome screen.")

    def intro_screen(self):
        intro = True
        start_button = StartGameButton(200, 200, 100, 50, AppConfig.WHITE, AppConfig.BLACK, 'Start', 32)
        while intro:
            for event in pygame.event.get():
                if event.type == QUIT:
                    intro = False
                    self.running = False

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if start_button.is_pressed(mouse_pos, mouse_pressed):
                intro = False
                self._start_simulation()

            start_button.draw(self.screen)
            pygame.display.update()
