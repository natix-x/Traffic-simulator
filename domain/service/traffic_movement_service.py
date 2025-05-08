from domain.entities import Intersection
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from domain.aggregates.traffic_system import TrafficSystem


class TrafficMovementService:
    def __init__(self, traffic_system: "TrafficSystem"):
        self.traffic_system = traffic_system

    def move_vehicles(self, intersection: Intersection):
        for position, queue in intersection.waiting_vehicles.items():
            while queue:
                light = self._get_light(intersection, position)
                if light is None or not light.is_green():
                    break

                vehicle = intersection.get_next_vehicle(position)
                intersection.move_vehicle_into_intersection(position)
                vehicle.move()

    def _get_light(self, intersection: Intersection, position):
        for light in self.traffic_system.traffic_lights.values():
            if light.intersection == intersection and light.position == position:
                return light
        return None
