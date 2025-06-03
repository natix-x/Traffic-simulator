from simulation.domain.entities import Intersection, TrafficLight

from simulation.domain.models import Position, TrafficLightState
from simulation.domain.models.intersection_type import IntersectionType
from simulation.domain.models.lights_switch_strategy import LightsSwitchStrategy
from simulation.domain.services.lights_switching_strategies.opposite_directions_green import OppositeDirectionsGreen
from simulation.domain.services.lights_switching_strategies.single_direction_green import SingleDirectionGreen
from simulation.domain.services.priority.traffic_lights_intersection_rule import TrafficLightsIntersectionRule


class TrafficLightsIntersection(Intersection):
    def __init__(self, switching_strategy: LightsSwitchStrategy):
        super().__init__()
        self.traffic_lights = {d: [] for d in Position}
        self.switching_strategy = switching_strategy
        self._initial_traffic_lights_setup()
        self.add_priority_rules()
        self.type = IntersectionType.TRAFFIC_LIGHTS_INTERSECTION

    def _initial_traffic_lights_setup(self):
        if self.switching_strategy == LightsSwitchStrategy.OPPOSITE_DIRECTIONS_GREEN:
            lights = OppositeDirectionsGreen.initial_traffic_lights_setup()
        else:
            lights = SingleDirectionGreen.initial_traffic_lights_setup()
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
