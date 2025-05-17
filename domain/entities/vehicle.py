import uuid

from domain.entities.intersection import Intersection
from domain.models import VehicleDirection, VehicleType, Position, VehicleState
from ui.resources.images.vehicle_images import VEHICLE_IMAGES


class Vehicle:
    def __init__(self, vehicle_type: VehicleType, speed: int, current_intersection: Intersection,
                 current_position: Position, direction: VehicleDirection):
        self.type = vehicle_type
        self.speed = speed
        self.current_intersection = current_intersection
        self.current_position = current_position
        self.direction = direction
        self.current_state = VehicleState.APPROACH
        self.id = uuid.uuid4()
        self.x, self.y = self._calculate_initial_coordinates()
        self.image = self._image()

    POSITION_TRANSITIONS = {
        (Position.N, VehicleDirection.STRAIGHT): Position.N,
        (Position.N, VehicleDirection.LEFT): Position.W,
        (Position.N, VehicleDirection.RIGHT): Position.E,

        (Position.S, VehicleDirection.STRAIGHT): Position.S,
        (Position.S, VehicleDirection.LEFT): Position.E,
        (Position.S, VehicleDirection.RIGHT): Position.W,

        (Position.E, VehicleDirection.STRAIGHT): Position.E,
        (Position.E, VehicleDirection.LEFT): Position.N,
        (Position.E, VehicleDirection.RIGHT): Position.S,

        (Position.W, VehicleDirection.STRAIGHT): Position.W,
        (Position.W, VehicleDirection.LEFT): Position.S,
        (Position.W, VehicleDirection.RIGHT): Position.N,
    }

    def change_position(self):
        key = (self.current_position, self.direction)
        self.current_position = self.POSITION_TRANSITIONS[key]
        self.current_state = VehicleState.EXITED

        if self.direction != VehicleDirection.STRAIGHT:
            self.image = self._image()

    def __str__(self):
        return f"{self.type.name}({self.id}) at {self.current_position} going {self.direction}"

    def move(self):
        self._go_forward(self.current_position)

        if self.current_state == VehicleState.APPROACH and self._is_at_the_stop_line():
            self.current_state = VehicleState.AT_STOP_LINE

        elif self.current_state == VehicleState.AT_STOP_LINE:
            self.current_state = VehicleState.IN_INTERSECTION

        elif self.current_state == VehicleState.IN_INTERSECTION and self._should_change_position():
            self.change_position()

    def _calculate_initial_coordinates(self):
        position = self.current_position
        return {
            Position.S: (290, 500),
            Position.N: (210, 6),
            Position.E: (490, 220),
            Position.W: (0, 290),
        }[position]

    def _image(self):
        return VEHICLE_IMAGES[self.current_position][self.type]

    def _go_forward(self, position: Position):
        if position == Position.S:
            self.y -= self.speed
        elif position == Position.N:
            self.y += self.speed
        elif position == Position.E:
            self.x -= self.speed
        elif position == Position.W:
            self.x += self.speed

    def _is_at_the_stop_line(self) -> bool:
        return (
            (self.current_position == Position.N and self.y >= 120) or
            (self.current_position == Position.S and self.y <= 360) or
            (self.current_position == Position.E and self.x <= 360) or
            (self.current_position == Position.W and self.x >= 120)
        )

    def _should_change_position(self) -> bool:
        pos = self.current_position

        if self.direction == VehicleDirection.RIGHT:
            return (
                (pos == Position.N and self.y >= 220) or
                (pos == Position.S and self.y <= 280) or
                (pos == Position.E and self.x <= 280) or
                (pos == Position.W and self.x >= 220)
            )
        else:
            return (
                (pos == Position.N and self.y >= 300) or
                (pos == Position.S and self.y <= 200) or
                (pos == Position.E and self.x <= 200) or
                (pos == Position.W and self.x >= 300)
            )

    def exit_intersection(self):
        if self._has_exited_intersection():
            self.current_state = VehicleState.EXITED

    def _has_exited_intersection(self) -> bool:
        pos = self.current_position

        return (
                (pos == Position.N and self.y >= 350) or
                (pos == Position.S and self.y <= 150) or
                (pos == Position.E and self.x <= 150) or
                (pos == Position.W and self.x >= 350)
        )

