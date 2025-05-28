import uuid
from typing import TYPE_CHECKING
from abc import ABCMeta, abstractmethod, ABC

from domain.models import Position

if TYPE_CHECKING:
    from domain.entities.vehicle import Vehicle


class Intersection(ABC):

    def __init__(self):
        self.id = uuid.uuid4()
        self.vehicles = {d: [] for d in Position}
        self.priority_rule = None

    def add_vehicle(self, vehicle: "Vehicle"):
        self.vehicles[vehicle.current_position].append(vehicle)

    @abstractmethod
    def add_priority_rules(self):
        raise NotImplementedError
