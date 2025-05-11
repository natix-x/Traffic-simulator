import uuid
from dataclasses import dataclass, field

from domain.entities.intersection import Intersection
from domain.models import VehicleDirection, VehicleType, Position, VehicleState
from ui.resources.images.vehicle_images import VEHICLE_IMAGES


# Dostosowano do jednego skrzyżowania TODO: rozbudować do wielu
# @dataclass
class Vehicle:
    # # current_route: list[Intersection]   TODO: wykorzystaj później do wielu skrzyżowań;

    def __init__(self, type: VehicleType, speed: int, current_intersection: Intersection,
                          current_position: Position, direction: VehicleDirection):
        self.type = type
        self.speed = speed
        self.current_intersection = current_intersection
        self.current_position = current_position
        self.direction = direction
        self.current_state = VehicleState.APPROACH
        self.id = field(default_factory=uuid.uuid4)
        self.x, self.y = self._calculate_initial_coordinates()
        self.image = self._image()

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

    def set_coordinates(self, x,y):
        self.x = x
        self.y = y

    def change_position(self):
        """Changes the vehicle position according to its initial position and desired direction"""
        if self.direction and self.current_position:
            key = (self.current_position, self.direction)
            self.current_position = self.POSITION_TRANSITIONS[key]
            self.current_state = VehicleState.EXITED
            if self.direction != VehicleDirection.STRAIGHT:
                self.image = self._image()


    def __str__(self):
        return f"{self.type.name}({self.id}) at {self.current_position} going {self.direction}"


    def move(self):
        position = self.current_position

        self._go_forward(position)

        if self.current_state == VehicleState.APPROACH:
            if self.y >= 200 and position == Position.N:
                self.current_state = VehicleState.IN_INTERSECTION

            if self.x <= 300 and position == Position.E:
                self.current_state = VehicleState.IN_INTERSECTION

            if self.y <= 300 and position == Position.S:
                self.current_state = VehicleState.IN_INTERSECTION

            if self.x >= 200 and position == Position.W:
                self.current_state = VehicleState.IN_INTERSECTION

        if self.current_state == VehicleState.IN_INTERSECTION:
            if self.direction != VehicleDirection.RIGHT: # chyba gdzieś jest błąd logiczny bo tutaj powinno być left, ale działa right
                self.change_position()
            elif (self.y >= 296 and position == Position.N) or (self.y <= 204 and position == Position.S) or (self.x <= 204 and position == Position.E) or (self.x >= 296 and position == Position.W):
                self.change_position()



    # TODO: nie zardcodować wartości - obliczać dynamicznie, dodać logikę jak więcej skrzyżowań
    def _calculate_initial_coordinates(self):
        position = self.current_position
        if position == Position.S:
            return 290, 500
        elif position == Position.N:
            return 210, 6
        elif position == Position.E:
            return 490, 220
        elif position == Position.W:
            return 0, 290

    def _image(self):
        position = self.current_position
        type = self.type
        return VEHICLE_IMAGES[position][type]

    def _go_forward(self, position: Position):
        if position == Position.S:
            self.y -= 2 #self.vehicle.speed
        elif position == Position.N:
            self.y += 2 #self.vehicle.speed
        elif position == Position.E:
            self.x -= 2 #self.vehicle.speed
        elif position == Position.W:
            self.x += 2 #self.vehicle.speed


