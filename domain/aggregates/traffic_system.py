from dataclasses import dataclass, field
from random import choice
from uuid import UUID

from domain.entities import Intersection, TrafficLight, Vehicle, TrafficLightsIntersection
from domain.entities.equal_intersection import EqualIntersection
from domain.models import TrafficLightState, VehicleType, Position, VehicleDirection


@dataclass
class TrafficSystem:
    intersections: dict[UUID, Intersection] = field(default_factory=dict)
    traffic_lights: dict[UUID, TrafficLight] = field(default_factory=dict)
    vehicles: dict[UUID, Vehicle] = field(default_factory=dict)

    def add_vehicle(self, vehicle: Vehicle):
        self.vehicles[vehicle.id] = vehicle
        intersection = choice(list(self.intersections.values()))
        intersection.add_vehicle(vehicle)

    def add_traffic_light(self, traffic_light: TrafficLight):
        self.traffic_lights[traffic_light.id] = traffic_light

    def _add_intersection(self, intersection: Intersection):
        self.intersections[intersection.id] = intersection

    def update_traffic_light(self, traffic_light_id: UUID, new_state: TrafficLightState):
        self.traffic_lights[traffic_light_id].change_state(new_state)

    def generate_random_car(self):
        vehicle = Vehicle(vehicle_type=choice(list(VehicleType)),
                          speed=4,
                          current_intersection=choice(list(self.intersections.values())),
                          current_position=choice(list(Position)),
                          direction=choice(list(VehicleDirection)))
        self.add_vehicle(vehicle)

    def add_traffic_lights_intersection(self, intersection: TrafficLightsIntersection):
        self._add_intersection(intersection)
        for light in intersection.get_all_traffic_lights():
            self.add_traffic_light(light)

    def add_equal_intersection(self, intersection: EqualIntersection):
        self._add_intersection(intersection)
