from typing import TYPE_CHECKING
from domain.models import VehicleDirection, Position
from domain.services.priority.priority_rules import PriorityRules

if TYPE_CHECKING:
    from domain.entities import TrafficLightsIntersection


class TrafficLightsIntersectionRule(PriorityRules):
    def __init__(self):
        self.intersection = None

    def set_context(self, *, intersection: "TrafficLightsIntersection"):
        self.intersection = intersection

    def should_give_way(self, vehicle) -> bool:
        if vehicle.direction == VehicleDirection.RIGHT:
            return False

        right_position = super().get_right_position(vehicle)

        for other in self.intersection.vehicles[right_position]:
            if other == vehicle:
                continue

            if self._is_green_light(right_position):
                if super().distance_between(vehicle, other) < 60:
                    return True

        return False

    def _is_green_light(self, position: Position) -> bool:
        return self.intersection.traffic_lights[position].is_green()
