from enum import Enum


class VehicleState(Enum):
    """Current vehicle's state on the intersection."""
    APPROACH = "approach"
    AT_STOP_LINE = "at_stop_line"
    IN_INTERSECTION = "in_intersection"
    EXITED = "exited"

    def __str__(self):
        return self.value
