from domain.aggregates.traffic_system import TrafficSystem
from domain.models import TrafficLightState
from domain.entities import Vehicle


class TrafficControl:
    def __init__(self, traffic_system: TrafficSystem):
        self.traffic_system = traffic_system

    def update_traffic_lights(self):  # poprawa logiki działania świateł w symulacji, początkowo jedne światła na raz mogą być zielone
        for light in self.traffic_system.traffic_lights.values():
            if light.state == TrafficLightState.RED:
                light.change_state(TrafficLightState.GREEN)
            elif light.state == TrafficLightState.GREEN:
                light.change_state(TrafficLightState.YELLOW)
            elif light.state == TrafficLightState.YELLOW:
                light.change_state(TrafficLightState.RED)

