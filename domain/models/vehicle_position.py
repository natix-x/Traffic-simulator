from enum import Enum


class VehiclePosition(Enum):
    N = "N"
    E = "E"
    S = "S"
    W = "W"

    def __str__(self):
        return self.value
