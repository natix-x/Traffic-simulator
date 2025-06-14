import random
from typing import TYPE_CHECKING

from simulation.domain.entities import TrafficLight
from simulation.domain.models import Position, TrafficLightState
from simulation.domain.services.lights_switching_strategies.lights_switch_strategy import LightsSwitchStrategy

if TYPE_CHECKING:
    from simulation.domain.entities import TrafficLightsIntersection


class SingleFixedCycle(LightsSwitchStrategy):

    def __init__(self, intersection: "TrafficLightsIntersection"):
        super().__init__(intersection)

    @staticmethod
    def initial_traffic_lights_setup() -> list[TrafficLight]:
        rand_position = random.choice([Position.N, Position.S, Position.E, Position.W])
        lights = []

        for pos in list(Position):
            if pos == rand_position:
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
        green_found = False
        lights = list(self.intersection.traffic_lights.values())
        for i, light in enumerate(lights):
            light.state_timer += 1
            if light.state == TrafficLightState.GREEN and light.state_timer >= self.intersection.light_duration:
                light.change_state(TrafficLightState.RED)
                next_index = (i + 1) % len(lights)
                green_found = True
                break

        if green_found:
            lights[next_index].change_state(TrafficLightState.GREEN)
