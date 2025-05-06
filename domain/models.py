from enum import Enum


class TrafficLightState(Enum):
    RED = "RED"
    GREEN = "GREEN"
    YELLOW = "YELLOW"

    def __str__(self):
        return self.value


class Direction(Enum):
    STRAIGHT = "STRAIGHT"
    LEFT = "LEFT"
    RIGHT = "RIGHT"

    def __str__(self):
        return self.value


class VehicleType(Enum):
    CAR = "CAR",
    BUS = "BUS",
    TAXI = "TAXI",
    BIKE = "BIKE"
