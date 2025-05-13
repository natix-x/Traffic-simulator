import uuid
from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from domain.models import Position

if TYPE_CHECKING:
    from domain.entities.vehicle import Vehicle


@dataclass
class Intersection:
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    vehicles: dict[Position, list["Vehicle"]] = field(default_factory=lambda: {d: [] for d in Position})

    def add_vehicle(self, vehicle: "Vehicle"):
        self.vehicles[vehicle.current_position].append(vehicle)
