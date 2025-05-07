from enum import Enum


class VehicleDirection(Enum):
    """Possible movement directions for a vehicle at an intersection."""
    STRAIGHT = "STRAIGHT"
    LEFT = "LEFT"
    RIGHT = "RIGHT"

    def __str__(self):
        return self.value
