import os

import pygame

from domain.entities import Vehicle
from domain.models import VehicleType


class VehicleRender:
    def __init__(self, vehicle: Vehicle, image: pygame.surface, screen: pygame.surface):
        self.vehicle = vehicle
        self.screen = screen

    def render(self):
        self.screen.blit(self.vehicle.image, (self.vehicle.x, self.vehicle.y))
        #if self.vehicle.type == VehicleType.POLICE:
        #    crash_sound = pygame.mixer.Sound(os.path.join("ui", "resources", "sounds", "police_siren.wav"))
        #    pygame.mixer.Sound.play(crash_sound)