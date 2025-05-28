import os

import pygame

from config import SimulationConfig
from domain.models.intersection_type import IntersectionType
from domain.models.lights_switch_strategy import LightsSwitchStrategy
from ui.buttons.custom_button import CustomButton
from ui.presenters.simulation_screen import SimulationScreen


class ConfigScreen:
    def __init__(self, screen):
        self.running = True
        self.screen = screen
        self.main_font = pygame.font.Font(os.path.join("ui", "resources", "ARIAL.ttf"), 20)
        pygame.display.set_caption("Configuration screen")

        self.intersection_type = 0
        self.strategy = None
        self.vehicles_per_second = 1
        self.slider = pygame.Rect(100, 300, 150, 5)
        self.handle = pygame.Rect(100, 290, 10, 20)
        self.dragging = False

        self.intersection_types_buttons = [
            CustomButton(100, 100, 100, 40, (0, 0, 0), (255, 255, 255), "Traffic Lights", 15),
            CustomButton(220, 100, 100, 40, (0, 0, 0), (255, 255, 255), "Equal", 15),
        ]

        self.strategy_buttons = [
            CustomButton(100, 200, 100, 40, (0, 0, 0), (255, 255, 255), "Opposite", 15),
            CustomButton(220, 200, 100, 40, (0, 0, 0), (255, 255, 255), "Single", 15),
            CustomButton(340, 200, 120, 40, (0, 0, 0), (255, 255, 255), "Most Cars", 15),
        ]

        self.start_button = CustomButton(100, 400, 200, 50, (0, 0, 0), (255, 255, 255), "Start", 20)

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

        for j, button in enumerate(self.strategy_buttons):
            if j == self.strategy:
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

        self.screen.blit(self.main_font.render(f"Vehicles / s: {self.vehicles_per_second}", True, (255, 255, 255)),
                         (100, 250))
        pygame.draw.rect(self.screen, (255, 255, 255), self.slider)
        pygame.draw.rect(self.screen, (200, 200, 200), self.handle)

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
                            if i == 1:
                                self.strategy = None

                    if self.intersection_type == 0:
                        for i, button in enumerate(self.strategy_buttons):
                            if button.is_pressed((x, y), pygame.mouse.get_pressed()):
                                self.strategy = i

                    if self.start_button.is_pressed((x, y), pygame.mouse.get_pressed()):
                        SimulationScreen(self.screen, self._get_chosen_config())

                    if self.handle.collidepoint(x, y):
                        self.dragging = True

                elif e.type == pygame.MOUSEBUTTONUP:
                    self.dragging = False

                elif e.type == pygame.MOUSEMOTION and self.dragging:
                    mx = max(self.slider.x, min(e.pos[0], self.slider.x + self.slider.width))
                    self.handle.x = mx
                    self.vehicles_per_second = 1 + (self.handle.x - self.slider.x) // 20

    def _get_chosen_config(self):

        intersection_type = None
        if self.intersection_type == 0:
            intersection_type = IntersectionType.TRAFFIC_LIGHTS_INTERSECTION
        elif self.intersection_type == 1:
            intersection_type = IntersectionType.EQUAL_INTERSECTION

        strategy = None
        if self.strategy is not None:
            if self.strategy == 0:
                strategy = LightsSwitchStrategy.OPPOSITE_DIRECTIONS_GREEN
            elif self.strategy == 1:
                strategy = LightsSwitchStrategy.SINGLE_DIRECTION_GREEN
            elif self.strategy == 2:
                strategy = LightsSwitchStrategy.MOST_CARS_GREEN

        return SimulationConfig(vehicles_per_second=self.vehicles_per_second,
                                intersection_type=intersection_type,
                                lights_switch_strategy=strategy)
