import os
import threading

import pygame
from pygame.locals import *

from application.simulation_engine import SimulationEngine
from domain.aggregates.traffic_system import TrafficSystem
from domain.entities import Intersection
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

    def _start_simulation(self):
        simulation_thread = threading.Thread(
            target=self._run_simulation_logic, daemon=True
        )
        simulation_thread.start()
        pygame.display.set_caption("Simulation")
        while self.running:
            self.screen.blit(self.background, (0, 0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
            pygame.display.update()
        pygame.quit()

    def _run_simulation_logic(self):
        traffic_system = TrafficSystem()
        intersection = Intersection()
        traffic_system.add_intersection(intersection)
        engine = SimulationEngine(traffic_system, tick_duration=1.0)
        engine.run(ticks=20)
