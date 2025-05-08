from domain.entities import Vehicle
from domain.models import Position
import pygame


class VehicleRender:
    def __init__(self, vehicle: Vehicle, image: pygame.surface, screen: pygame.surface):
        self.vehicle_position = vehicle.current_position
        self.image = image
        self.screen = screen

    def render(self):
        coordinates = self._calculate_coordinates()
        self.screen.blit(self.image, coordinates)

    # TODO: nie zardcodować wartości - obliczać dynamicznie, dodać logikę jak więcej skrzyżowań
    def _calculate_coordinates(self):
        if self.vehicle_position == Position.S:
            return 290, 500
        elif self.vehicle_position == Position.N:
            return 210, 6
        elif self.vehicle_position == Position.E:
            return 490, 220
        elif self.vehicle_position == Position.W:
            return 0, 290
