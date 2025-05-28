from domain.aggregates.traffic_system import TrafficSystem
from domain.models import TrafficLightState, Position
from domain.services.vehicle_movement import VehicleMovement


class IntersectionController:
    def __init__(self, traffic_system: TrafficSystem):
        self.traffic_system = traffic_system

    def update_traffic_lights(self):
        for light in self.traffic_system.traffic_lights.values():
            light.state_timer += 1
            if light.state == TrafficLightState.RED and light.state_timer >= 5:
                light.change_state(TrafficLightState.GREEN)
            elif light.state == TrafficLightState.GREEN and light.state_timer >= 5:
                light.change_state(TrafficLightState.YELLOW)
            elif light.state == TrafficLightState.YELLOW and light.state_timer >= 3:
                light.change_state(TrafficLightState.RED)

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
