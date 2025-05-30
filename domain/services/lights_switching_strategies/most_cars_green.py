import random
from typing import TYPE_CHECKING

from domain.entities import TrafficLight
from domain.models import Position, TrafficLightState
from domain.services.lights_switching_strategies.lights_switch_strategy import LightsSwitchStrategy

if TYPE_CHECKING:
    from domain.aggregates.traffic_system import TrafficSystem


class MostCarsGreen(LightsSwitchStrategy):
    def __init__(self, traffic_system: "TrafficSystem"):
        super().__init__(traffic_system)

    def initial_traffic_lights_setup(self):
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
        ...
