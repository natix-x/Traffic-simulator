from domain.aggregates.traffic_system import TrafficSystem
from domain.entities import Vehicle, TrafficLightsIntersection
from domain.models import VehicleDirection, Position, VehicleState
import math


class VehicleMovement:
    VEHICLE_GAP = 70

    def __init__(self, vehicle: Vehicle, traffic_system: TrafficSystem):
        self.vehicle = vehicle
        self.traffic_system = traffic_system
        self.current_intersection = vehicle.current_intersection
        self.current_position = vehicle.current_position

    @staticmethod
    def _distance_between(v1: Vehicle, v2: Vehicle) -> float:
        dx = v1.x - v2.x
        dy = v1.y - v2.y
        return math.sqrt(dx * dx + dy * dy)

    def _can_make_intersection_move(self) -> bool:
        if self._is_vehicle_in_front_of():
            return False
        right_pos = self._get_right_position()
        left_pos = self._get_left_position()
        return self._is_space_around_clear([right_pos, left_pos])

    def can_move(self) -> bool:
        if type(self.current_intersection) == TrafficLightsIntersection:
            green_light = self._is_green_light(self.current_position)

        if self._can_make_intersection_move():

            if type(self.current_intersection) == TrafficLightsIntersection:

                if self.vehicle.current_state == VehicleState.AT_STOP_LINE and not green_light:
                    return False

            if self.current_intersection.priority_rule.should_give_way(self.vehicle):
                return False

            return True

        return False

    def _get_right_position(self) -> Position:
        return {
            Position.N: Position.W,
            Position.E: Position.N,
            Position.S: Position.E,
            Position.W: Position.S,
        }[self.current_position]

    def _get_left_position(self) -> Position:
        return {
            Position.N: Position.E,
            Position.E: Position.S,
            Position.S: Position.W,
            Position.W: Position.N,
        }[self.current_position]

    def _is_vehicle_in_front_of(self) -> bool:
        for other in self.current_intersection.vehicles[self.current_position]:
            if other == self.vehicle:
                continue

            if self.current_position == Position.S and other.y < self.vehicle.y and self.vehicle.y - other.y < self.VEHICLE_GAP:
                return True
            elif self.current_position == Position.N and other.y > self.vehicle.y and other.y - self.vehicle.y < self.VEHICLE_GAP:
                return True
            elif self.current_position == Position.W and other.x > self.vehicle.x and other.x - self.vehicle.x < self.VEHICLE_GAP:
                return True
            elif self.current_position == Position.E and other.x < self.vehicle.x and self.vehicle.x - other.x < self.VEHICLE_GAP:
                return True

        return False

    def _is_space_around_clear(self, positions_to_check: list[Position]) -> bool:

        for pos in positions_to_check:
            for other in self.current_intersection.vehicles[pos]:
                if other == self.vehicle:
                    continue

                if self._distance_between(self.vehicle, other) < self.VEHICLE_GAP and self._is_in_relative_direction(
                        other, pos):
                    return False

        return True

    def _is_in_relative_direction(self, other: Vehicle, position: Position) -> bool:
        dx = other.x - self.vehicle.x
        dy = other.y - self.vehicle.y

        if position == Position.W:
            return dx > 0 and abs(dy) < self.VEHICLE_GAP
        if position == Position.E:
            return dx < 0 and abs(dy) < self.VEHICLE_GAP
        if position == Position.N:
            return dy > 0 and abs(dx) < self.VEHICLE_GAP
        if position == Position.S:
            return dy < 0 and abs(dx) < self.VEHICLE_GAP
        return False

    def _is_green_light(self, position: Position) -> bool:
        return self.current_intersection.traffic_lights[position].is_green()
