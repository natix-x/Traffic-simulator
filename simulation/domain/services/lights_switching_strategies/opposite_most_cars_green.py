import random
from abc import abstractmethod
from collections import defaultdict

from simulation.domain.entities import TrafficLight
from simulation.domain.models import TrafficLightState, Position
from simulation.domain.services.lights_switching_strategies.lights_switch_strategy import LightsSwitchStrategy
from simulation.domain.services.lights_switching_strategies.most_cars_green import MostCarsGreen
from simulation.domain.services.lights_switching_strategies.opposite_directions.opposite_fixed_cycle import \
    OppositeFixedCycle
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from simulation.domain.aggregates.traffic_system import TrafficSystem


class OppositeMostCarsGreen(MostCarsGreen):
    def __init__(self, traffic_system: "TrafficSystem"):
        super().__init__(traffic_system)
        self.waiting_number = defaultdict(int)

    @staticmethod
    def initial_traffic_lights_setup() -> list[TrafficLight]:
        return OppositeFixedCycle.initial_traffic_lights_setup()

    def update_traffic_lights(self):
        greens_found = 0
        lights = list(self.traffic_system.traffic_lights.values())
        for i, light in enumerate(lights):
            light.state_timer += 1
            if light.state == TrafficLightState.GREEN and light.state_timer >= self.traffic_system.config.light_duration:
                light.change_state(TrafficLightState.RED)
                greens_found += 1
                if greens_found == 2:
                    break

        if greens_found:
            next_green_pos = self.choose_next_green_position()
            opposite_next_green_pos = self._get_opposite_position(next_green_pos)
            next_greens = [next_green_pos, opposite_next_green_pos]
            if not next_green_pos:
                next_greens = random.sample((list(Position)), 2)
            for traffic_light in self.traffic_system.traffic_lights.values():
                if traffic_light.position in next_greens:
                    traffic_light.change_state(TrafficLightState.GREEN)

    @abstractmethod
    def choose_next_green_position(self) -> Position:
        raise NotImplementedError

    @staticmethod
    def _get_opposite_position(pos: Position) -> Position:
        return {
            Position.S: Position.N,
            Position.N: Position.S,
            Position.E: Position.W,
            Position.W: Position.E,
        }[pos]
