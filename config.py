from dataclasses import dataclass

from domain.models.intersection_type import IntersectionType
from domain.models.lights_switch_strategy import LightsSwitchStrategy


@dataclass
class AppConfig:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    WIDTH = 512
    HEIGHT = 512
    FPS = 30


@dataclass
class SimulationConfig:
    vehicles_per_second: int
    intersection_type: IntersectionType
    lights_switch_strategy: LightsSwitchStrategy = None
    light_duration: int = None
