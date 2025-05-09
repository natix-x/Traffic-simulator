from dataclasses import dataclass


@dataclass
class AppConfig:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    WINDOW_SIZE = (512, 512)
    FPS = 30


@dataclass
class SimulationConfig:
    ...
