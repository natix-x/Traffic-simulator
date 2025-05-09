import uuid
from dataclasses import dataclass, field

from domain.entities.intersection import Intersection
from domain.models import VehicleDirection, VehicleType, Position, VehicleState


# Dostosowano do jednego skrzyżowania TODO: rozbudować do wielu
@dataclass
class Vehicle:
    type: VehicleType
    speed: int
    # current_route: list[Intersection]   TODO: wykorzystaj później do wielu skrzyżowań;
    current_intersection: Intersection # które skrzyżowanie
    current_position: Position  # który pas
    direction: VehicleDirection  # który kierunek jazdy
    x: int = 0  # współrzędna x
    y: int = 0  # współrzędna y
    current_state: VehicleState = VehicleState.APPROACH  # czy pojazd jest na skrzyżowaniu, przed, czy za
    id: uuid.UUID = field(default_factory=uuid.uuid4)

    POSITION_TRANSITIONS = {
        # From North
        (Position.N, VehicleDirection.STRAIGHT): Position.N,
        (Position.N, VehicleDirection.LEFT): Position.E,
        (Position.N, VehicleDirection.RIGHT): Position.W,

        # From South
        (Position.S, VehicleDirection.STRAIGHT): Position.S,
        (Position.S, VehicleDirection.LEFT): Position.W,
        (Position.S, VehicleDirection.RIGHT): Position.E,

        # From East
        (Position.E, VehicleDirection.STRAIGHT): Position.E,
        (Position.E, VehicleDirection.LEFT): Position.S,
        (Position.E, VehicleDirection.RIGHT): Position.N,

        # From West
        (Position.W, VehicleDirection.STRAIGHT): Position.W,
        (Position.W, VehicleDirection.LEFT): Position.N,
        (Position.W, VehicleDirection.RIGHT): Position.S,
    }

    def move(self):
        """Changes the vehicle position according to its initial position and desired direction"""
        if self.direction and self.current_position and self.current_state == VehicleState.IN_INTERSECTION:
            key = (self.current_position, self.direction)
            self.current_position = self.POSITION_TRANSITIONS[key]
            self.current_state = VehicleState.EXITED

    def __str__(self):
        return f"{self.type.name}({self.id}) at {self.current_position} going {self.direction}"
