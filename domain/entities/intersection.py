import uuid
from typing import TYPE_CHECKING

from domain.models import Position

if TYPE_CHECKING:
    from domain.entities.vehicle import Vehicle


class Intersection:
    def __init__(self):
        self.id = uuid.uuid4()
        self.vehicles = {d: [] for d in Position}

    def add_vehicle(self, vehicle: "Vehicle"):
        self.vehicles[vehicle.current_position].append(vehicle)
