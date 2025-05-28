from domain.aggregates.traffic_system import TrafficSystem
from domain.services.traffic_control import IntersectionController


class SimulationEngine:
    def __init__(self, traffic_system: TrafficSystem):
        self.traffic_system = traffic_system
        self.traffic_control = IntersectionController(self.traffic_system)

    def update_movement(self):
        self.traffic_control.move_all_vehicles()

    def update_lights(self):
        self.traffic_control.update_traffic_lights()

    def generate_vehicles(self):
        for _ in range(1):
            self.traffic_system.generate_random_car()
