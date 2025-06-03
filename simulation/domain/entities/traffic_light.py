import uuid
from dataclasses import field

from simulation.domain.entities.intersection import Intersection
from simulation.domain.models import TrafficLightState, Position


class TrafficLight:
    def __init__(self, state: TrafficLightState, position: Position):
        self.state = state
        self.position = position
        self.id = uuid.uuid4()
        self.state_timer = 0

    def change_state(self, new_state: TrafficLightState):
        self.state = new_state
        self.state_timer = 0

    def is_green(self):
        return self.state == TrafficLightState.GREEN
