from random import choice
from uuid import UUID

from config import SimulationConfig, AppConfig
from domain.entities import Intersection, TrafficLight, Vehicle, TrafficLightsIntersection
from domain.entities.equal_intersection import EqualIntersection
from domain.models import TrafficLightState, VehicleType, Position, VehicleDirection
from domain.models.intersection_type import IntersectionType


class TrafficSystem:
    def __init__(self, config: SimulationConfig):
        self.config = config
        self.intersections: dict[UUID, Intersection] = {}
        self.traffic_lights: dict[UUID, TrafficLight] = {}
        self.vehicles: dict[UUID, Vehicle] = {}
        self.create_initial_system()

    def create_initial_system(self):
        if self.config.intersection_type == IntersectionType.TRAFFIC_LIGHTS_INTERSECTION:
            self.add_traffic_lights_intersection(TrafficLightsIntersection(self.config.lights_switch_strategy))
        elif self.config.intersection_type == IntersectionType.EQUAL_INTERSECTION:
            self.add_equal_intersection(EqualIntersection())

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

    def update_vehicles_list(self, intersection: Intersection):
        vehicles_to_remove = []

        for vehicles_list in intersection.vehicles.values():
            for vehicle in vehicles_list:
                if vehicle.x > AppConfig.WIDTH or vehicle.y > AppConfig.HEIGHT:
                    vehicles_to_remove.append(vehicle)

        for vehicle in vehicles_to_remove:
            intersection.delete_vehicle(vehicle)
            self.vehicles.pop(vehicle.id)
