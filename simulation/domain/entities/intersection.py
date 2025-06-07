import uuid
from typing import TYPE_CHECKING
from abc import abstractmethod, ABC

from simulation.domain.models import Position
from simulation.domain.models.intersection_type import IntersectionType
from simulation.domain.services.priority.priority_rules import PriorityRules

if TYPE_CHECKING:
    from simulation.domain.entities.vehicle import Vehicle


class Intersection(ABC):

    def __init__(self):
        self.id = uuid.uuid4()
        self.vehicles: dict[Position, list["Vehicle"]] = {d: [] for d in Position}
        self.priority_rule: PriorityRules | None = None
        self.type: IntersectionType | None = None
        self.vehicles_in_intersection = 0
        self.vehicles_passed = 0

    def add_vehicle(self, vehicle: "Vehicle"):
        self.vehicles[vehicle.current_position].append(vehicle)

    @abstractmethod
    def add_priority_rules(self):
        raise NotImplementedError

    def delete_vehicle(self, vehicle: "Vehicle"):
        self.vehicles[vehicle.current_position].remove(vehicle)
