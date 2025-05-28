from domain.aggregates.traffic_system import TrafficSystem
from domain.models import TrafficLightState, Position
from domain.models.intersection_type import IntersectionType
from domain.models.lights_switch_strategy import LightsSwitchStrategy
from domain.services.lights_switching_strategies.opposite_directions_green import OppositeDirectionsGreen
from domain.services.lights_switching_strategies.single_direction_green import SingleDirectionGreen
from domain.services.vehicle_movement import VehicleMovement


class IntersectionController:
    def __init__(self, traffic_system: TrafficSystem):
        self.traffic_system = traffic_system

    def update_traffic_lights(self):
        for intersection in self.traffic_system.intersections.values():
            if intersection.type == IntersectionType.TRAFFIC_LIGHTS_INTERSECTION:

                if intersection.switching_strategy == LightsSwitchStrategy.OPPOSITE_DIRECTIONS_GREEN:
                    OppositeDirectionsGreen.update_traffic_lights(self.traffic_system)

                elif intersection.switching_strategy == LightsSwitchStrategy.SINGLE_DIRECTION_GREEN:
                    SingleDirectionGreen.update_traffic_lights(self.traffic_system)

    def move_all_vehicles(self):
        for intersection in self.traffic_system.intersections.values():
            updated_vehicles = {pos: [] for pos in Position}
            for position, vehicles in intersection.vehicles.items():
                for vehicle in vehicles:
                    vehicle_movement = VehicleMovement(vehicle, self.traffic_system)
                    if vehicle_movement.can_move():
                        vehicle.move()
                    updated_vehicles[vehicle.current_position].append(vehicle)

            intersection.vehicles = updated_vehicles
