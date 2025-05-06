import uuid
from dataclasses import dataclass, field

from domain.entities.intersection import Intersection
from domain.models import VehicleDirection, VehicleType, VehiclePosition


@dataclass
class Vehicle:  # TODO: ID MUSI BYĆ UNIKLANE w ramach jednej symulacji
    type: VehicleType
    speed: int
    # current_route: list[Intersection]   TODO: wykorzystaj później do wielu skrzyżowań;
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    current_intersection: Intersection | None = None  # które skrzyżowanie
    current_position: VehiclePosition | None = None  # który pas, z której strony
    direction: VehicleDirection | None = None  # do tetsowania dla jednego skrzyżowania

    def move(self):
        if self.direction and self.current_position:
            if self.direction == VehicleDirection.STRAIGHT:
                # TODO: logika poruszania się prosto
                print(f"Vehicle {self.id} is going straight")
            elif self.direction == VehicleDirection.LEFT:
                # TODO: logika skrętu w lewo
                print(f"Vehicle {self.id} is turning left")
            elif self.direction == VehicleDirection.RIGHT:
                # TODO: logika skrętu w prawo
                print(f"Vehicle {self.id} is turning right")
