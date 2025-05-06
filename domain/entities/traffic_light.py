from dataclasses import dataclass
from domain.entities.intersection import Intersection
from domain.models import TrafficLightState


@dataclass
class TrafficLight:
    id: str
    state: TrafficLightState
    intersection: Intersection

    def change_state(self, new_state: TrafficLightState):
        self.state = new_state


def traffic_light_factory(id: str, state: TrafficLightState, intersection: Intersection) -> TrafficLight:
    return TrafficLight(id=id, state=state, intersection=intersection)