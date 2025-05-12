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
    INTERSECTION_WIDTH = 512
    CENTER_X = INTERSECTION_WIDTH // 2
    CENTER_Y = INTERSECTION_WIDTH // 2
    APPROACH_THRESHOLD = 0.75
    TURN_THRESHOLD = 0.9
