from dataclasses import dataclass
from domain.entities import Intersection, TrafficLight, Vehicle
from domain.models import TrafficLightState


@dataclass
class TrafficSystem:
    intersections: dict[str, Intersection]
    traffic_lights: dict[str, TrafficLight]
    vehicles: dict[str, Vehicle]

    def add_vehicle(self, vehicle: Vehicle):
        self.vehicles[vehicle.id] = vehicle

    def add_traffic_light(self, traffic_light: TrafficLight):
        self.traffic_lights[traffic_light.id] = traffic_light

    def add_intersection(self, intersection: Intersection):
        self.intersections[intersection.id] = intersection

    def update_traffic_light(self, traffic_light_id: str, new_state: TrafficLightState):
        self.traffic_lights[traffic_light_id].change_state(new_state)

    def move_vehicle(self, vehicle_id: str):
        vehicle = self.vehicles[vehicle_id]
        vehicle.move()
