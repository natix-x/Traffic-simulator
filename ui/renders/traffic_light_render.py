import pygame

from domain.entities import TrafficLight
from domain.models import Position, TrafficLightState
import os


# logika dostosowana do jednego skrzyżowania, TODO: dostosować do wielu
class TrafficLightRender:
    def __init__(self, traffic_light: TrafficLight, screen: pygame.surface):
        self.traffic_light = traffic_light
        self.image = None
        self.screen = screen
        self.x, self.y = self._calculate_coordinates()

    def render(self):
        self._update_image()
        self.screen.blit(self.image, (self.x, self.y))

    def _update_image(self):
        lights_images = os.path.join("ui", "resources", "images", "lights")
        if self.traffic_light.state == TrafficLightState.RED:
            self.image = pygame.transform.scale(
                pygame.image.load(os.path.join(lights_images, "red_light.png")), (20, 50)
            )
        elif self.traffic_light.state == TrafficLightState.GREEN:
            self.image = pygame.transform.scale(
                pygame.image.load(os.path.join(lights_images, "green_light.png")), (20, 50)
            )
        elif self.traffic_light.state == TrafficLightState.YELLOW:
            self.image = pygame.transform.scale(
                pygame.image.load(os.path.join(lights_images, "yellow_light.png")), (20, 50)
            )

    # TODO: nie zardcodować wartości - obliczać dynamicznie
    def _calculate_coordinates(self):
        position = self.traffic_light.position
        if position == Position.S:
            return 344, 344
        elif position == Position.N:
            return 146, 118
        elif position == Position.E:
            return 344, 118
        elif position == Position.W:
            return 146, 344
