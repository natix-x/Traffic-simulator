import uuid
from dataclasses import dataclass, field

# from domain.entities import Vehicle, vehicle
from domain.models import Position, VehicleState


@dataclass
class Intersection:
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    # waiting_vehicles: dict[Position, list[Vehicle]] = field(default_factory=lambda: {d: [] for d in Position})
    #
    # def add_vehicle(self, vehicle: Vehicle):
    #     self.waiting_vehicles[vehicle.current_position].append(vehicle)
    #
    # def get_next_vehicle(self, position: Position) -> Vehicle | None:
    #     if self.waiting_vehicles[position]:
    #         return self.waiting_vehicles[position][0]
    #     return None
    #
    # def move_vehicle_into_intersection(self, position: Position):
    #     vehicle = self.get_next_vehicle(position)
    #     if vehicle:
    #         self.waiting_vehicles[position].pop(0)
    #         vehicle.current_state = VehicleState.IN_INTERSECTION
