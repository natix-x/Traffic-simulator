from enum import Enum


class Position(Enum):
    """Tells on which lane the object is located."""
    N = "N"
    E = "E"
    S = "S"
    W = "W"

    def __str__(self):
        return self.value
