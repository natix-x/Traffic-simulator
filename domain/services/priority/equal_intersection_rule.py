from typing import TYPE_CHECKING

from domain.models import VehicleDirection
from domain.services.priority.priority_rules import PriorityRules

if TYPE_CHECKING:
    if TYPE_CHECKING:
        from domain.entities import EqualIntersection


class EqualIntersectionRule(PriorityRules):
    def __init__(self):
        self.intersection = None

    def set_context(self, *, intersection: "EqualIntersection"):
        self.intersection = intersection

    def should_give_way(self, vehicle) -> bool:
        if vehicle.direction == VehicleDirection.RIGHT:
            return False

        right_position = super().get_right_position(vehicle)

        for other in self.intersection.vehicles[right_position]:
            if other == vehicle:
                continue

            if super().distance_between(vehicle, other) < 40:
                return True

        return False
