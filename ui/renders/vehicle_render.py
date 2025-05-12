import pygame

from domain.entities import Vehicle


class VehicleRender:
    def __init__(self, vehicle: Vehicle, image: pygame.surface, screen: pygame.surface):
        self.vehicle = vehicle
        self.screen = screen

    def render(self):
        self.screen.blit(self.vehicle.image, (self.vehicle.x, self.vehicle.y))