from simulation.domain.entities import Intersection, TrafficLight

from simulation.domain.models import Position
from simulation.domain.models.intersection_type import IntersectionType
from simulation.domain.models.lights_switch_strategy import LightsSwitchStrategy
from simulation.domain.services.lights_switching_strategies import *

from simulation.domain.services.priority.traffic_lights_intersection_rule import TrafficLightsIntersectionRule


class TrafficLightsIntersection(Intersection):
    def __init__(self, switching_strategy: LightsSwitchStrategy, light_duration: int):
        super().__init__()
        self.traffic_lights = {d: [] for d in Position}
        self.switching_strategy = self._choose_switching_lights_strategy(switching_strategy)
        self._initial_traffic_lights_setup()
        self.add_priority_rules()
        self.light_duration = light_duration
        self.type = IntersectionType.TRAFFIC_LIGHTS_INTERSECTION

    def _initial_traffic_lights_setup(self):
        lights = self.switching_strategy.initial_traffic_lights_setup()
        for light in lights:
            self._add_traffic_light(light)

    def _add_traffic_light(self, traffic_light: TrafficLight):
        self.traffic_lights[traffic_light.position] = traffic_light

    def get_all_traffic_lights(self) -> list[TrafficLight]:
        return list(self.traffic_lights.values())

    def add_priority_rules(self):
        priority_rule = TrafficLightsIntersectionRule()
        priority_rule.set_context(intersection=self)
        self.priority_rule = priority_rule

    def _choose_switching_lights_strategy(self, strategy: LightsSwitchStrategy):
        if strategy == LightsSwitchStrategy.OPPOSITE_FIXED_CYCLE:
            return OppositeFixedCycle(self)
        elif strategy == LightsSwitchStrategy.SINGLE_FIXED_CYCLE:
            return SingleFixedCycle(self)
        elif strategy == LightsSwitchStrategy.SINGLE_MOST_CARS:
            return SingleMostCars(self)
        elif strategy == LightsSwitchStrategy.SINGLE_MOST_CARS_WAITING:
            return SingleMostCarsWaiting(self)
        elif strategy == LightsSwitchStrategy.SINGLE_MAX_WAITING:
            return SingleMaxWaiting(self)
        elif strategy == LightsSwitchStrategy.OPPOSITE_MOST_CARS:
            return OppositeMostCars(self)
        elif strategy == LightsSwitchStrategy.OPPOSITE_MOST_CARS_WAITING:
            return OppositeMostCarsWaiting(self)
        elif strategy == LightsSwitchStrategy.OPPOSITE_MAX_WAITING:
            return OppositeMaxWaiting(self)
