from domain.aggregates.traffic_system import TrafficSystem
from domain.models import TrafficLightState


# TODO: refaktoryzacja
def update_traffic_lights(traffic_system: TrafficSystem):
    for light in traffic_system.traffic_lights.values():
        if light.state == TrafficLightState.RED:
            light.change_state(TrafficLightState.GREEN)
        elif light.state == TrafficLightState.GREEN:
            light.change_state(TrafficLightState.YELLOW)
        elif light.state == TrafficLightState.YELLOW:
            light.change_state(TrafficLightState.RED)
