import random
from abc import abstractmethod
from collections import defaultdict
from typing import TYPE_CHECKING

from simulation.domain.entities import TrafficLight
from simulation.domain.models import Position, TrafficLightState
from simulation.domain.services.lights_switching_strategies.most_cars_green import MostCarsGreen
from simulation.domain.services.lights_switching_strategies.single_direction.single_fixed_cycle import SingleFixedCycle

if TYPE_CHECKING:
    from simulation.domain.entities import TrafficLight, TrafficLightsIntersection


class SingleMostCarsGreen(MostCarsGreen):
    def __init__(self, intersection: "TrafficLightsIntersection"):
        super().__init__(intersection)
        self.waiting_number = defaultdict(int)

    @staticmethod
    def initial_traffic_lights_setup() -> list[TrafficLight]:
        return SingleFixedCycle.initial_traffic_lights_setup()

    def update_traffic_lights(self):
        green_found = False
        lights = list(self.intersection.traffic_lights.values())
        for i, light in enumerate(lights):
            light.state_timer += 1
            if light.state == TrafficLightState.GREEN and light.state_timer >= self.intersection.light_duration:
                light.change_state(TrafficLightState.RED)
                green_found = True
                break

        if green_found:
            next_green_pos = self.choose_next_green_position()
            if not next_green_pos:
                next_green_pos = random.choice(list(Position))
            for traffic_light in self.intersection.traffic_lights.values():
                if traffic_light.position == next_green_pos:
                    traffic_light.change_state(TrafficLightState.GREEN)

    @abstractmethod
    def choose_next_green_position(self) -> Position:
        raise NotImplementedError

