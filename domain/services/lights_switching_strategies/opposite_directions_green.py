from typing import TYPE_CHECKING
from domain.entities import TrafficLight
from domain.models import Position, TrafficLightState
import random
if TYPE_CHECKING:
    from domain.aggregates.traffic_system import TrafficSystem


class OppositeDirectionsGreen:

    @staticmethod
    def initial_traffic_lights_setup():
        rand_positions = random.choice([[Position.N, Position.S], [Position.E, Position.W]])
        lights = []
        for pos in list(Position):
            if pos in rand_positions:
                lights.append(TrafficLight(
                    state=TrafficLightState.GREEN,
                    position=pos
                ))
            else:
                lights.append(TrafficLight(
                    state=TrafficLightState.RED,
                    position=pos
                ))

        return lights

    @staticmethod
    def update_traffic_lights(traffic_system: "TrafficSystem"):
        for light in traffic_system.traffic_lights.values():
            light.state_timer += 1
            if light.state == TrafficLightState.RED and light.state_timer >= 5:
                light.change_state(TrafficLightState.GREEN)
            elif light.state == TrafficLightState.GREEN and light.state_timer >= 5:
                light.change_state(TrafficLightState.YELLOW)
            elif light.state == TrafficLightState.YELLOW and light.state_timer >= 3:
                light.change_state(TrafficLightState.RED)
