from enum import Enum


class VehicleType(Enum):
    CAR = "CAR"
    BUS = "BUS"
    BIKE = "BIKE"
    TRACK = "TRACK"

    def __str__(self):
        return self.value
