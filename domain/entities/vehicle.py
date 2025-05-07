import uuid
from dataclasses import dataclass, field

from domain.entities.intersection import Intersection
from domain.models import VehicleDirection, VehicleType, Position


# Dostosowano do jednego skrzyżowania TODO: rozbudować do wielu
@dataclass
class Vehicle:
    type: VehicleType
    speed: int
    # current_route: list[Intersection]   TODO: wykorzystaj później do wielu skrzyżowań;
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    current_intersection: Intersection | None = None  # które skrzyżowanie
    current_position: Position | None = None  # który pas
    direction: VehicleDirection | None = None  # który kierunek jazdy

    POSITION_TRANSITIONS = {
        # From North
        (Position.N, VehicleDirection.STRAIGHT): Position.S,
        (Position.N, VehicleDirection.LEFT): Position.E,
        (Position.N, VehicleDirection.RIGHT): Position.W,

        # From South
        (Position.S, VehicleDirection.STRAIGHT): Position.N,
        (Position.S, VehicleDirection.LEFT): Position.W,
        (Position.S, VehicleDirection.RIGHT): Position.E,

        # From East
        (Position.E, VehicleDirection.STRAIGHT): Position.W,
        (Position.E, VehicleDirection.LEFT): Position.S,
        (Position.E, VehicleDirection.RIGHT): Position.N,

        # From West
        (Position.W, VehicleDirection.STRAIGHT): Position.E,
        (Position.W, VehicleDirection.LEFT): Position.N,
        (Position.W, VehicleDirection.RIGHT): Position.S,
    }

    def move(self):
        """Changes the vehicle position according to its initial position and desired direction"""
        if self.direction and self.current_position:
            key = (self.current_position, self.direction)
            self.current_position = self.POSITION_TRANSITIONS[key]
