from domain.aggregates.traffic_system import TrafficSystem
from domain.entities import Intersection, Vehicle
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
            updated_vehicles = {pos: [] for pos in Position}  # ← tutaj!

            for position, vehicles in intersection.vehicles.items():
                for vehicle in vehicles:
                    allow_move = False
                    if not self._is_vehicle_before(vehicle):
                        if self._is_green_light(intersection, position):
                            allow_move = True
                        elif vehicle.current_state != VehicleState.AT_STOP_LINE:
                            allow_move = True

                    if allow_move:
                        vehicle.move()

                    new_position = vehicle.current_position
                    updated_vehicles[new_position].append(vehicle)

            intersection.vehicles = updated_vehicles

    def _is_green_light(self, intersection: Intersection, position: Position) -> bool:
        for traffic_light in self.traffic_system.traffic_lights.values():
            if traffic_light.position == position and traffic_light.intersection == intersection:
                return traffic_light.is_green()

    @staticmethod
    def _is_vehicle_before(vehicle: Vehicle) -> bool:
        position = vehicle.current_position
        intersection = vehicle.current_intersection

        min_distance = float("inf")

        for other in intersection.vehicles[position]:
            if other == vehicle:
                continue

            if position == Position.S and other.y < vehicle.y:
                distance = vehicle.y - other.y
            elif position == Position.N and other.y > vehicle.y:
                distance = other.y - vehicle.y
            elif position == Position.W and other.x > vehicle.x:
                distance = other.x - vehicle.x
            elif position == Position.E and other.x < vehicle.x:
                distance = vehicle.x - other.x
            else:
                continue
            if distance < min_distance:
                min_distance = distance

        return min_distance < 40


