from domain.entities import Intersection
from typing import TYPE_CHECKING

from domain.models import VehicleState

if TYPE_CHECKING:
    from domain.aggregates.traffic_system import TrafficSystem


# TODO: sprawdzenie działania logiki tego
class TrafficMovementService:
    def __init__(self, traffic_system: "TrafficSystem"):
        self.traffic_system = traffic_system

    def move_vehicles(self, intersection: Intersection):
        for position, queue in intersection.waiting_vehicles.items():
            pass

    # def move_vehicles(self, intersection: Intersection):
    #     for position, queue in intersection.waiting_vehicles.items():
    #         light = self._get_light(intersection, position)
    #         if light is None or not light.is_green():
    #             continue
    #         for vehicle in queue:
    #             if vehicle.current_state == VehicleState.IN_INTERSECTION:
    #                 vehicle.move()

    def _get_light(self, intersection: Intersection, position):
        for light in self.traffic_system.traffic_lights.values():
            if light.intersection == intersection and light.position == position:
                return light
        return None
