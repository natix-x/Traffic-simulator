from domain.aggregates.traffic_system import TrafficSystem
from domain.models import TrafficLightState
from domain.services.movement_service import MovementService


class TrafficControl:
    def __init__(self, traffic_system: TrafficSystem):
        self.traffic_system = traffic_system
        self.movement_service = MovementService(traffic_system)

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
        self.movement_service.move_all_vehicles()
