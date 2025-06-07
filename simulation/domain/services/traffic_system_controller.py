from simulation.domain.aggregates.traffic_system import TrafficSystem
from simulation.domain.entities import Vehicle
from simulation.domain.models import Position, VehicleState
from simulation.domain.models.intersection_type import IntersectionType
from simulation.domain.services.vehicle_movement import VehicleMovement


class TrafficSystemController:
    def __init__(self, traffic_system: TrafficSystem):
        self.traffic_system = traffic_system

    def update_traffic_lights(self):
        for intersection in self.traffic_system.intersections.values():
            if intersection.type == IntersectionType.TRAFFIC_LIGHTS_INTERSECTION:
                intersection.switching_strategy.update_traffic_lights()

    def move_all_vehicles(self):
        for intersection in self.traffic_system.intersections.values():
            updated_vehicles = {pos: [] for pos in Position}
            for position, vehicles in intersection.vehicles.items():
                for vehicle in vehicles:
                    vehicle_movement = VehicleMovement(vehicle, self.traffic_system)
                    if vehicle_movement.can_move():
                        vehicle.move()
                        if not vehicle.counted_in_intersection and vehicle.current_state == VehicleState.IN_INTERSECTION:
                            intersection.vehicles_in_intersection += 1
                            vehicle.counted_in_intersection = True

                        elif vehicle.counted_in_intersection and vehicle.current_state == VehicleState.EXITED:
                            intersection.vehicles_in_intersection -= 1
                            vehicle.counted_in_intersection = False
                    else:
                        if vehicle.current_state in [VehicleState.APPROACH, VehicleState.AT_STOP_LINE]:
                            vehicle.waiting_time += 1

                    updated_vehicles[vehicle.current_position].append(vehicle)

            intersection.vehicles = updated_vehicles
            self.traffic_system.update_vehicles_list(intersection)
