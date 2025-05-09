import uuid
from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from domain.models import Position, VehicleState

if TYPE_CHECKING:
    from domain.entities.vehicle import Vehicle


@dataclass
class Intersection:
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    waiting_vehicles: dict[Position, list["Vehicle"]] = field(default_factory=lambda: {d: [] for d in Position})

    def add_vehicle(self, vehicle: "Vehicle"):
        self.waiting_vehicles[vehicle.current_position].append(vehicle)
