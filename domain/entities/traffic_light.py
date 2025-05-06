import uuid
from dataclasses import dataclass, field

from domain.entities.intersection import Intersection
from domain.models import TrafficLightState


@dataclass
class TrafficLight:
    state: TrafficLightState
    intersection: Intersection
    id: uuid.UUID = field(default_factory=uuid.uuid4)

    def change_state(self, new_state: TrafficLightState):
        self.state = new_state
