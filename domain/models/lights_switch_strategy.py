from enum import Enum


class LightsSwitchStrategy(Enum):
    OPPOSITE_DIRECTIONS_GREEN = "OPPOSITE_DIRECTIONS_GREEN"
    SINGLE_DIRECTION_GREEN = "SINGLE_DIRECTION_GREEN"
    MOST_CARS_GREEN = "MOST_CARS_GREEN"

    def __str__(self):
        return self.value
