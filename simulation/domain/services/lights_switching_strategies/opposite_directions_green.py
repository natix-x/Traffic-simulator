import random
from typing import TYPE_CHECKING

from simulation.domain.entities import TrafficLight
from simulation.domain.models import Position, TrafficLightState
from simulation.domain.services.lights_switching_strategies.lights_switch_strategy import LightsSwitchStrategy

if TYPE_CHECKING:
    from simulation.domain.aggregates.traffic_system import TrafficSystem


class OppositeDirectionsGreen(LightsSwitchStrategy):
    def __init__(self, traffic_system: "TrafficSystem"):
        super().__init__(traffic_system)

    @staticmethod
    def initial_traffic_lights_setup() -> list[TrafficLight]:
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

    def update_traffic_lights(self):
        for light in self.traffic_system.traffic_lights.values():
            light.state_timer += 1
            if light.state == TrafficLightState.RED and light.state_timer >= self.traffic_system.config.light_duration:
                light.change_state(TrafficLightState.GREEN)
            elif light.state == TrafficLightState.GREEN and light.state_timer >= self.traffic_system.config.light_duration:
                light.change_state(TrafficLightState.YELLOW)
            elif light.state == TrafficLightState.YELLOW and light.state_timer >= 1:
                light.change_state(TrafficLightState.RED)
