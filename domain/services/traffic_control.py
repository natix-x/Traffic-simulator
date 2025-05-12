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
            for position, vehicles in intersection.waiting_vehicles.items():
                if self._is_green_light(intersection, position):
                    for vehicle in vehicles:
                        vehicle.move()
                else:
                    for vehicle in vehicles:
                        if vehicle.current_state != VehicleState.AT_STOP_LINE:
                            vehicle.move()

    def _is_green_light(self, intersection: Intersection, position: Position) -> bool:
        for traffic_light in self.traffic_system.traffic_lights.values():
            if traffic_light.position == position and traffic_light.intersection == intersection:
                return traffic_light.is_green()

