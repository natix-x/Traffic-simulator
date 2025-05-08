from dataclasses import dataclass
from random import choice, randint
from uuid import UUID

from domain.entities import Intersection, TrafficLight, Vehicle
from domain.models import TrafficLightState, VehicleType, Position, VehicleDirection
from domain.service.traffic_movement_service import TrafficMovementService


# TODO: zmień defualty
@dataclass
class TrafficSystem:
    intersections: dict[UUID, Intersection] | None = None
    traffic_lights: dict[UUID, TrafficLight] | None = None
    vehicles: dict[UUID, Vehicle] | None = None
    movement_service: TrafficMovementService | None = None


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

    def step_simulation(self):
        for intersection in self.intersections.values():
            self.movement_service.move_vehicles(intersection)
