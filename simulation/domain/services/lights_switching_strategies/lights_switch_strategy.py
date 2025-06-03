from abc import ABCMeta, abstractmethod
from typing import TYPE_CHECKING

from simulation.domain.entities import TrafficLight

if TYPE_CHECKING:
    from simulation.domain.aggregates.traffic_system import TrafficSystem


class LightsSwitchStrategy(metaclass=ABCMeta):

    def __init__(self, traffic_system: "TrafficSystem"):
        self.traffic_system = traffic_system

    @staticmethod
    @abstractmethod
    def initial_traffic_lights_setup() -> list[TrafficLight]:
        raise NotImplementedError

    @abstractmethod
    def update_traffic_lights(self):
        raise NotImplementedError
