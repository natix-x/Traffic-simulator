import math

from domain.aggregates.traffic_system import TrafficSystem
from domain.entities import Vehicle, TrafficLightsIntersection
from domain.models import TrafficLightState, VehicleState, Position, VehicleDirection


# TODO: refaktoryzacja
class TrafficControl:
    def __init__(self, traffic_system: TrafficSystem):
        self.traffic_system = traffic_system

    def update_traffic_lights(self):
        for light in self.traffic_system.traffic_lights.values():
            light.state_timer += 1
            if light.state == TrafficLightState.RED and light.state_timer >= 5:
                light.change_state(TrafficLightState.GREEN)
            elif light.state == TrafficLightState.GREEN and light.state_timer >= 5:
                light.change_state(TrafficLightState.YELLOW)
            elif light.state == TrafficLightState.YELLOW and light.state_timer >= 3:
                light.change_state(TrafficLightState.RED)

    def move_all_vehicles(self):
        for intersection in self.traffic_system.intersections.values():
            updated_vehicles = {pos: [] for pos in Position}

            for position, vehicles in intersection.vehicles.items():
                for vehicle in vehicles:
                    allow_move = self._can_vehicle_move(vehicle)
                    if allow_move:
                        vehicle.move()
                    updated_vehicles[vehicle.current_position].append(vehicle)

            intersection.vehicles = updated_vehicles

        return True

    def _is_green_light(self, lights_intersection: TrafficLightsIntersection, position: Position) -> bool:
        return lights_intersection.traffic_lights[position].is_green()

    def _is_vehicle_before(self, vehicle: Vehicle) -> bool:
        position = vehicle.current_position
        intersection = vehicle.current_intersection

        for other in intersection.vehicles[position]:
            if other == vehicle:
                continue

            if position == Position.S and other.y < vehicle.y and vehicle.y - other.y < 60:
                return True
            elif position == Position.N and other.y > vehicle.y and other.y - vehicle.y < 60:
                return True
            elif position == Position.W and other.x > vehicle.x and other.x - vehicle.x < 60:
                return True
            elif position == Position.E and other.x < vehicle.x and vehicle.x - other.x < 60:
                return True

        return False

    def _should_give_way(self, vehicle: Vehicle) -> bool:
        if vehicle.direction == VehicleDirection.RIGHT:
            return False

        position = vehicle.current_position
        intersection = vehicle.current_intersection
        right_position = self._get_right_position(position)

        for other in intersection.vehicles[right_position]:
            if other == vehicle:
                continue

            if self._is_green_light(intersection, right_position):
                if self._distance_between(vehicle, other) < 70:
                    return True

        return False

    @staticmethod
    def _get_right_position(position: Position) -> Position:
        return {
            Position.N: Position.W,
            Position.E: Position.N,
            Position.S: Position.E,
            Position.W: Position.S,
        }[position]

    @staticmethod
    def _get_left_position(position: Position) -> Position:
        return {
            Position.N: Position.E,
            Position.E: Position.S,
            Position.S: Position.W,
            Position.W: Position.N,
        }[position]

    @staticmethod
    def _distance_between(v1: Vehicle, v2: Vehicle) -> float:
        dx = v1.x - v2.x
        dy = v1.y - v2.y
        return math.sqrt(dx * dx + dy * dy)

    def _can_vehicle_move(self, vehicle: Vehicle) -> bool:
        if self._is_vehicle_before(vehicle):
            return False

        intersection = vehicle.current_intersection
        position = vehicle.current_position
        green_light = self._is_green_light(intersection, position)

        if vehicle.current_state == VehicleState.AT_STOP_LINE and not green_light:
            return False

        if not green_light and self._should_give_way(vehicle):
            return False

        if vehicle.direction == VehicleDirection.STRAIGHT:
            return self._can_go_straight(vehicle)
        else:
            return self._can_turn(vehicle)

    def _is_space_around_clear(self, vehicle: Vehicle, positions_to_check: list[Position],
                               distance_threshold: float = 50) -> bool:
        intersection = vehicle.current_intersection
        vx, vy = vehicle.x, vehicle.y

        for pos in positions_to_check:
            for other in intersection.vehicles[pos]:
                if other == vehicle:
                    continue

                dx = other.x - vx
                dy = other.y - vy

                if pos == Position.W:
                    if 0 < dx < distance_threshold and abs(dy) < distance_threshold:
                        return False
                elif pos == Position.E:
                    if -distance_threshold < dx < 0 and abs(dy) < distance_threshold:
                        return False
                elif pos == Position.N:
                    if 0 < dy < distance_threshold and abs(dx) < distance_threshold:
                        return False
                elif pos == Position.S:
                    if -distance_threshold < dy < 0 and abs(dx) < distance_threshold:
                        return False

        return True

    def _can_turn(self, vehicle: Vehicle) -> bool:
        right_pos = self._get_right_position(vehicle.current_position)
        left_pos = self._get_left_position(vehicle.current_position)
        return self._is_space_around_clear(vehicle, [right_pos, left_pos])

    def _can_go_straight(self, vehicle: Vehicle) -> bool:
        right_pos = self._get_right_position(vehicle.current_position)
        left_pos = self._get_left_position(vehicle.current_position)
        return self._is_space_around_clear(vehicle, [right_pos, left_pos])
