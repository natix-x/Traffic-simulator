import os

import pygame

from simulation.config import SimulationConfig
from simulation.domain.models.intersection_type import IntersectionType
from simulation.domain.models.lights_switch_strategy import LightsSwitchStrategy
from simulation.ui.buttons.custom_button import CustomButton
from simulation.ui.presenters.simulation_screen import SimulationScreen


class ConfigScreen:
    def __init__(self, screen):
        self.running = True
        self.screen = screen
        self.main_font = pygame.font.Font(os.path.join("simulation", "ui", "resources", "ARIAL.ttf"), 20)
        pygame.display.set_caption("Configuration screen")

        self.intersection_type = 0
        self.lights_strategy = 0
        self.vehicles_per_second = 1
        self.light_duration = 5
        self.slider_light_duration = pygame.Rect(100, 300, 150, 5)
        self.handle_light_duration = pygame.Rect(180, 290, 10, 20)
        self.dragging_light_duration = False
        self.slider_vehicles = pygame.Rect(100, 400, 150, 5)
        self.handle_vehicles = pygame.Rect(100, 390, 10, 20)
        self.dragging_vehicles = False

        self.intersection_types_buttons = [
            CustomButton(100, 100, 100, 40, (0, 0, 0), (255, 255, 255), "Traffic Lights", 15),
            CustomButton(220, 100, 100, 40, (0, 0, 0), (255, 255, 255), "Equal", 15),
        ]

        self.lights_strategy_buttons = [
            CustomButton(100, 200, 70, 40, (0, 0, 0), (255, 255, 255), "Opposite", 10),
            CustomButton(180, 200, 70, 40, (0, 0, 0), (255, 255, 255), "Single", 10),
            CustomButton(260, 200, 70, 40, (0, 0, 0), (255, 255, 255), "Most Cars Basic", 10),
            CustomButton(340, 200, 70, 40, (0, 0, 0), (255, 255, 255), "Most Cars Waiting", 10),
            CustomButton(420, 200, 70, 40, (0, 0, 0), (255, 255, 255), "Max Wait", 10),
        ]

        self.start_button = CustomButton(100, 450, 200, 50, (0, 0, 0), (255, 255, 255), "Start", 20)

        self.run()

    def draw(self):
        self.screen.fill((0, 0, 0))

        self.screen.blit(self.main_font.render("Intersection type:", True, (255, 255, 255)), (100, 60))

        for i, button in enumerate(self.intersection_types_buttons):
            if i == self.intersection_type:
                button.bg = (255, 255, 255)
                button.fg = (0, 0, 0)
            else:
                button.bg = (80, 80, 80)
                button.fg = (200, 200, 200)
            button.image.fill(button.bg)
            button.text = button.font.render(button.content, True, button.fg)
            button.text_rect = button.text.get_rect(center=(button.width / 2, button.height / 2))
            button.image.blit(button.text, button.text_rect)
            button.draw(self.screen)

        self.screen.blit(self.main_font.render("Traffic lights strategy:", True, (255, 255, 255)), (100, 160))

        for j, button in enumerate(self.lights_strategy_buttons):
            if j == self.lights_strategy:
                button.bg = (255, 255, 255)
                button.fg = (0, 0, 0)
            else:
                button.bg = (80, 80, 80)
                button.fg = (200, 200, 200)
            button.image.fill(button.bg)
            button.text = button.font.render(button.content, True, button.fg)
            button.text_rect = button.text.get_rect(center=(button.width / 2, button.height / 2))
            button.image.blit(button.text, button.text_rect)
            button.draw(self.screen)

        if self.intersection_type == 0:
            self.screen.blit(self.main_font.render(f"Light duration (s): {self.light_duration}", True, (255, 255, 255)),
                             (100, 250))
            pygame.draw.rect(self.screen, (255, 255, 255), self.slider_light_duration)
            pygame.draw.rect(self.screen, (200, 200, 200), self.handle_light_duration)
        else:
            self.screen.blit(self.main_font.render("Light duration (disabled for 'Equal')", True, (100, 100, 100)),
                             (100, 250))
            pygame.draw.rect(self.screen, (80, 80, 80), self.slider_light_duration)
            pygame.draw.rect(self.screen, (100, 100, 100), self.handle_light_duration)

        self.screen.blit(self.main_font.render(f"Vehicles / s: {self.vehicles_per_second}", True, (255, 255, 255)),
                         (100, 360))
        pygame.draw.rect(self.screen, (255, 255, 255), self.slider_vehicles)
        pygame.draw.rect(self.screen, (200, 200, 200), self.handle_vehicles)

        self.start_button.draw(self.screen)

        pygame.display.flip()

    def run(self):
        while self.running:
            self.draw()
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit();
                    exit()

                elif e.type == pygame.MOUSEBUTTONDOWN:
                    x, y = e.pos

                    for i, button in enumerate(self.intersection_types_buttons):
                        if button.is_pressed((x, y), pygame.mouse.get_pressed()):
                            self.intersection_type = i
                            if i == 0:
                                self.lights_strategy = 0
                            if i == 1:
                                self.lights_strategy = None
                                self.light_duration = None

                    if self.intersection_type == 0:
                        for i, button in enumerate(self.lights_strategy_buttons):
                            if button.is_pressed((x, y), pygame.mouse.get_pressed()):
                                self.lights_strategy = i

                    if self.start_button.is_pressed((x, y), pygame.mouse.get_pressed()):
                        SimulationScreen(self.screen, self._get_chosen_config())

                    if self.handle_vehicles.collidepoint(x, y):
                        self.dragging_vehicles = True

                    if self.handle_light_duration.collidepoint(x, y):
                        self.dragging_light_duration = True

                    if self.intersection_type == 0 and self.handle_light_duration.collidepoint(x, y):
                        self.dragging_light_duration = True

                elif e.type == pygame.MOUSEBUTTONUP:
                    self.dragging_vehicles = False
                    self.dragging_light_duration = False

                elif e.type == pygame.MOUSEMOTION and self.dragging_vehicles:
                    mx = max(self.slider_vehicles.x, min(e.pos[0], self.slider_vehicles.x + self.slider_vehicles.width))
                    self.handle_vehicles.x = mx
                    self.vehicles_per_second = 1 + (self.handle_vehicles.x - self.slider_vehicles.x) // 20

                elif e.type == pygame.MOUSEMOTION and self.dragging_light_duration and self.intersection_type == 0:
                    mx = max(self.slider_light_duration.x,
                             min(e.pos[0], self.slider_light_duration.x + self.slider_light_duration.width))
                    self.handle_light_duration.x = mx
                    self.light_duration = 1 + (self.handle_light_duration.x - self.slider_light_duration.x) // 20

    def _get_chosen_config(self) -> SimulationConfig:

        intersection_type = None
        if self.intersection_type == 0:
            intersection_type = IntersectionType.TRAFFIC_LIGHTS_INTERSECTION
        elif self.intersection_type == 1:
            intersection_type = IntersectionType.EQUAL_INTERSECTION

        strategy = None
        if self.lights_strategy is not None:
            if self.lights_strategy == 0:
                strategy = LightsSwitchStrategy.OPPOSITE_DIRECTIONS_GREEN
            elif self.lights_strategy == 1:
                strategy = LightsSwitchStrategy.SINGLE_DIRECTION_GREEN
            elif self.lights_strategy == 2:
                strategy = LightsSwitchStrategy.MOST_CARS_GREEN_BASIC
            elif self.lights_strategy == 3:
                strategy = LightsSwitchStrategy.MOST_CARS_GREEN_WAITING
            elif self.lights_strategy == 4:
                strategy = LightsSwitchStrategy.MAX_WAIT_GREEN

        return SimulationConfig(vehicles_per_second=self.vehicles_per_second,
                                intersection_type=intersection_type,
                                lights_switch_strategy=strategy,
                                light_duration=self.light_duration)
