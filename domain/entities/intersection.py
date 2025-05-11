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

    # dynamicznie zmieniające sie linie stopu w zależności od ilości czekających pojazdów
    stop_line_N = 90
    stop_line_E = 364
    stop_line_W = 116
    stop_line_S = 394


    def add_vehicle(self, vehicle: "Vehicle"):
        self.waiting_vehicles[vehicle.current_position].append(vehicle)

    def get_next_vehicle(self, position: Position): # -> "Vehicle" | None:
        if self.waiting_vehicles[position]:
            return self.waiting_vehicles[position][0]
        return None

    def move_vehicle_into_intersection(self, position: Position):
        vehicle = self.get_next_vehicle(position)
        if vehicle:
            self.waiting_vehicles[position].pop(0)
            vehicle.current_state = VehicleState.IN_INTERSECTION
