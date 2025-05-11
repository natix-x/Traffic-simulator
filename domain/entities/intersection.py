import uuid
from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from domain.models import Position, VehicleState

if TYPE_CHECKING:
    from domain.entities.vehicle import Vehicle


@dataclass
class Intersection:
    id: uuid.UUID = field(default_factory=uuid.uuid4)

    # dynamicznie zmieniające sie linie stopu w zależności od ilości czekających pojazdów
    stop_line_N = 90
    stop_line_E = 364
    stop_line_W = 116
    stop_line_S = 394

    vehicles: dict[Position, list["Vehicle"]] = field(default_factory=lambda: {d: [] for d in Position})

    def add_vehicle(self, vehicle: "Vehicle"):
        self.vehicles[vehicle.current_position].append(vehicle)

    # def