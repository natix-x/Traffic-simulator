from enum import Enum


class VehicleDirection(Enum):
    STRAIGHT = "STRAIGHT"
    LEFT = "LEFT"
    RIGHT = "RIGHT"

    def __str__(self):
        return self.value
