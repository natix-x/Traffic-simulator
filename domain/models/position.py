from enum import Enum


class VehiclePosition(Enum):
    """Vehicle's current lane."""
    N = "N"
    E = "E"
    S = "S"
    W = "W"

    def __str__(self):
        return self.value
