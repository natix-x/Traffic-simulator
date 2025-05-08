import pygame

from domain.entities import Vehicle
from domain.models import Position


class VehicleRender:
    def __init__(self, vehicle: Vehicle, image: pygame.surface, screen: pygame.surface):
        self.vehicle_position = vehicle.current_position
        self.image = image
        self.screen = screen
        self.x, self.y = self._calculate_initial_coordinates()

    def render(self):
        self.screen.blit(self.image, (self.x, self.y))

    def update(self):  # TODO: zaadoptować do logiki poruszania się, na razie jest jednostajnie
        if self.vehicle_position == Position.S:
            self.y -= 2
        elif self.vehicle_position == Position.N:
            self.y += 2
        elif self.vehicle_position == Position.E:
            self.x -= 2
        elif self.vehicle_position == Position.W:
            self.x += 2

    # TODO: nie zardcodować wartości - obliczać dynamicznie, dodać logikę jak więcej skrzyżowań
    def _calculate_initial_coordinates(self):
        if self.vehicle_position == Position.S:
            return 290, 500
        elif self.vehicle_position == Position.N:
            return 210, 6
        elif self.vehicle_position == Position.E:
            return 490, 220
        elif self.vehicle_position == Position.W:
            return 0, 290
