import uuid
from dataclasses import dataclass, field

from domain.entities.intersection import Intersection
from domain.models import TrafficLightState, Position


@dataclass
class TrafficLight:
    state: TrafficLightState
    intersection: Intersection
    position: Position  # każde skrzyżowanie będzie miało 4 światła
    id: uuid.UUID = field(default_factory=uuid.uuid4)

    def change_state(self, new_state: TrafficLightState):
        self.state = new_state

    def is_green(self):
        return self.state == TrafficLightState.GREEN
