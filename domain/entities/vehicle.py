from dataclasses import dataclass
from domain.entities.intersection import Intersection
from domain.models import Direction, VehicleType


@dataclass
class Vehicle:
    id: str
    type: VehicleType
    speed: int
    # current_route: list[Intersection]   TODO: wykorzystaj później do wielu skrzyżowań;
    # current_position: Intersection | None = None TODO: TODO: wykorzystaj później do wielu skrzyżowań
    direction: Direction | None = None # do tetsowania dla jednego skrzyżowania

    def move(self):
        if self.direction and self.current_position:
            if self.direction == Direction.STRAIGHT:
                # TODO: logika poruszania się prosto
                print(f"Vehicle {self.id} is going straight")
            elif self.direction == Direction.LEFT:
                # TODO: logika skrętu w lewo
                print(f"Vehicle {self.id} is turning right")
            elif self.direction == Direction.RIGHT:
                # TODO: logika skrętu w prawo
                print(f"Vehicle {self.id} is turning right")


def vehicle_factory(
    id: str, type: VehicleType, speed: int
) -> Vehicle:
    return Vehicle(id=id, type=type, speed=speed)