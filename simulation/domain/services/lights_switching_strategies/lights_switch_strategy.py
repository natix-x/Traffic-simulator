from abc import ABCMeta, abstractmethod
from typing import TYPE_CHECKING
from simulation.domain.entities import TrafficLight

if TYPE_CHECKING:
    from simulation.domain.entities import TrafficLightsIntersection


class LightsSwitchStrategy(metaclass=ABCMeta):

    def __init__(self, traffic_lights_intersection: "TrafficLightsIntersection"):
        self.intersection = traffic_lights_intersection

    @staticmethod
    @abstractmethod
    def initial_traffic_lights_setup() -> list[TrafficLight]:
        raise NotImplementedError

    @abstractmethod
    def update_traffic_lights(self):
        raise NotImplementedError
