import os

import pygame
from pygame.locals import *

from domain.entities import TrafficLight, Intersection
from domain.models import Position, TrafficLightState
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
        self.vehicle = pygame.transform.scale(
            pygame.image.load(os.path.join("ui", "resources", "images", "cars", "car_E.png")), (40, 25)
        )
        self._initialize_display()

    def _start_simulation(self):
        clock = pygame.time.Clock()
        dt = 0
        start_pos = pygame.Vector2(0, 296)
        intersection = Intersection()
        light = TrafficLight(state=TrafficLightState.RED, intersection=intersection, position=Position.W)
        light_time = 0

        # taffic_system = TrafficSystem()
        # traffic_system.add_traffic_light(light)
        # traffic_system.add_in

        while self.running:
            self.screen.blit(self.background, (0, 0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
            # pygame.display.update() # jak to jest to bardzo miga

            pygame.display.set_caption("Simulation")

            # lokalizacja świateł dla jednego skrzyżowania
            pygame.draw.circle(self.screen, 'red', (146, 146), 5)
            pygame.draw.circle(self.screen, 'red', (366, 146), 5)
            pygame.draw.circle(self.screen, 'red', (146, 366), 5)
            pygame.draw.circle(self.screen, 'red', (366, 366), 5)

            # pozycje pojazdów
            pygame.draw.circle(self.screen, 'blue', (216, 142), 20)
            #pygame.draw.circle(self.screen, 'blue', (142, 296), 20)
            pygame.draw.circle(self.screen, 'blue', (370, 216), 20)
            pygame.draw.circle(self.screen, 'blue', (296, 370), 20)

            # coś co działa
            self.screen.blit(self.vehicle, start_pos)
            pygame.display.flip()

            # zmiana pozycji - nie działa najlepiej
            if start_pos.x < 122 or (light.is_green() and start_pos.x >= 122):
                dt = clock.tick(60) / 10 # wolna basic prędkość -> szybsze można mnożyć przez coś >1
                start_pos.x = (start_pos.x + dt) % 512

            light_time += 1 # uzależnić od czasu
            if light_time % 500 == 0:
                if light.is_green():
                    light.change_state(TrafficLightState.RED)
                    print("red")
                else:
                    light.change_state(TrafficLightState.GREEN)



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
