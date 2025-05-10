from domain.aggregates.traffic_system import TrafficSystem
from domain.models import TrafficLightState
from domain.service.traffic_movement_service import TrafficMovementService


class TrafficControl:
    def __init__(self, traffic_system: TrafficSystem):
        self.traffic_system = traffic_system
        self.movement_service = TrafficMovementService(traffic_system)

    def update_traffic_lights(self):
        for light in self.traffic_system.traffic_lights.values():
            if light.state == TrafficLightState.RED:
                light.change_state(TrafficLightState.GREEN)
            elif light.state == TrafficLightState.GREEN:
                light.change_state(TrafficLightState.YELLOW)
            elif light.state == TrafficLightState.YELLOW:
                light.change_state(TrafficLightState.RED)

    def move_all_vehicles(self):
        for intersection in self.traffic_system.intersections.values():
            self.movement_service.move_vehicles(intersection)

