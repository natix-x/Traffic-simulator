from domain.aggregates.traffic_system import TrafficSystem
from domain.entities import Vehicle, TrafficLightsIntersection
from domain.models import TrafficLightState, VehicleState, Position


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
            elif light.state == TrafficLightState.YELLOW and light.state_timer >= 2:
                light.change_state(TrafficLightState.RED)

    def move_all_vehicles(self):
        for intersection in self.traffic_system.intersections.values():
            updated_vehicles = {pos: [] for pos in Position}

            for position, vehicles in intersection.vehicles.items():
                for vehicle in vehicles:
                    allow_move = True

                    if self._is_vehicle_before(vehicle):
                        allow_move = False
                    elif self._should_give_way(vehicle):
                        allow_move = False
                    elif vehicle.current_state == VehicleState.AT_STOP_LINE:
                        allow_move = self._is_green_light(intersection, position)

                    if allow_move:
                        vehicle.move()

                    updated_vehicles[vehicle.current_position].append(vehicle)

            intersection.vehicles = updated_vehicles

    def _is_green_light(self, lights_intersection: TrafficLightsIntersection, position: Position) -> bool:
        return lights_intersection.traffic_lights[position].is_green()

    @staticmethod
    def _is_vehicle_before(vehicle: Vehicle) -> bool:
        position = vehicle.current_position
        intersection = vehicle.current_intersection

        for other in intersection.vehicles[position]:
            if other == vehicle:
                continue

            if position == Position.S and other.y < vehicle.y and vehicle.y - other.y < 40:
                return True
            elif position == Position.N and other.y > vehicle.y and other.y - vehicle.y < 40:
                return True
            elif position == Position.W and other.x > vehicle.x and other.x - vehicle.x < 40:
                return True
            elif position == Position.E and other.x < vehicle.x and vehicle.x - other.x < 40:
                return True

        return False

    def _should_give_way(self, vehicle: Vehicle) -> bool:
        position = vehicle.current_position
        intersection = vehicle.current_intersection
        right_position = self._get_right_position(position)

        for other in intersection.vehicles[right_position]:
            if other == vehicle:
                continue

            if abs(vehicle.x - other.x) < 50 and abs(vehicle.y - other.y) < 50:
                return True

        return False

    @staticmethod
    def _get_right_position(position: Position) -> Position:
        return {
            Position.N: Position.E,
            Position.E: Position.S,
            Position.S: Position.W,
            Position.W: Position.N,
        }[position]