from dataclasses import dataclass, field
from random import choice, randint
from uuid import UUID

from domain.entities import Intersection, TrafficLight, Vehicle
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

    def add_intersection(self, intersection: Intersection):
        self.intersections[intersection.id] = intersection

    def update_traffic_light(self, traffic_light_id: UUID, new_state: TrafficLightState):
        self.traffic_lights[traffic_light_id].change_state(new_state)

    def generate_random_car(self):
        vehicle = Vehicle(type=choice(list(VehicleType)),
                          speed=randint(20, 100),
                          current_intersection=choice(list(self.intersections.values())),
                          current_position=choice(list(Position)),
                          direction=choice(list(VehicleDirection)))
        self.add_vehicle(vehicle)
