from domain.aggregates.traffic_system import TrafficSystem
from domain.entities import Intersection
from domain.models import Position


class MovementService:
    def __init__(self, traffic_system: TrafficSystem):
        self.traffic_system = traffic_system

    def move_all_vehicles(self):
        for intersection in self.traffic_system.intersections.values():
            for position, vehicles in intersection.waiting_vehicles.items():
                if self._is_green_light(intersection, position):
                    for vehicle in vehicles:
                        vehicle.move()

    def _is_green_light(self, intersection: Intersection, position: Position) -> bool:
        for traffic_light in self.traffic_system.traffic_lights.values():
            if traffic_light.position == position and traffic_light.intersection == intersection:
                return traffic_light.is_green()
