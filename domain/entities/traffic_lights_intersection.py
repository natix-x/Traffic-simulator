from domain.entities import Intersection, TrafficLight

from domain.models import Position, TrafficLightState
from domain.services.priority.traffic_lights_intersection_rule import TrafficLightsIntersectionRule


class TrafficLightsIntersection(Intersection):
    def __init__(self):
        super().__init__()
        self.traffic_lights = {d: [] for d in Position}
        self._initial_traffic_lights_setup()
        self.add_priority_rules()

    def _initial_traffic_lights_setup(self):
        for pos in list(Position):
            if pos in [Position.N, Position.S]:
                self._add_traffic_light(TrafficLight(
                    state=TrafficLightState.GREEN,
                    position=pos
                ))
            else:
                self._add_traffic_light(TrafficLight(
                    state=TrafficLightState.RED,
                    position=pos
                ))

    def _add_traffic_light(self, traffic_light: TrafficLight):
        self.traffic_lights[traffic_light.position] = traffic_light

    def get_all_traffic_lights(self) -> list[TrafficLight]:
        return list(self.traffic_lights.values())

    def add_priority_rules(self):
        priority_rule = TrafficLightsIntersectionRule()
        priority_rule.set_context(intersection=self)
        self.priority_rule = priority_rule
