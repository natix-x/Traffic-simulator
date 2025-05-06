from dataclasses import dataclass
from random import choice, randint
from uuid import UUID

from domain.entities import Intersection, TrafficLight, Vehicle
from domain.models import TrafficLightState, VehicleType, VehiclePosition


@dataclass
class TrafficSystem:
    intersections: dict[UUID, Intersection]
    traffic_lights: dict[UUID, TrafficLight]
    vehicles: dict[UUID, Vehicle]

    def add_vehicle(self, vehicle: Vehicle):
        self.vehicles[vehicle.id] = vehicle

    def add_traffic_light(self, traffic_light: TrafficLight):
        self.traffic_lights[traffic_light.id] = traffic_light

    def add_intersection(self, intersection: Intersection):
        self.intersections[intersection.id] = intersection

    def update_traffic_light(self, traffic_light_id: UUID, new_state: TrafficLightState):
        self.traffic_lights[traffic_light_id].change_state(new_state)

    def move_vehicle(self, vehicle_id: UUID):
        vehicle = self.vehicles[vehicle_id]
        vehicle.move()

    def generate_random_car(self):
        vehicle = Vehicle(type=choice(list(VehicleType)),
                          speed=randint(20, 100),
                          current_intersection=choice(list(self.intersections.values())),
                          current_position=choice(list(VehiclePosition)),
                          direction=choice(list(VehiclePosition)))
        self.add_vehicle(vehicle)
