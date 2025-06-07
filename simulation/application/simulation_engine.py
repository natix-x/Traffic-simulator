from simulation.domain.aggregates.traffic_system import TrafficSystem
from simulation.domain.services.traffic_system_controller import TrafficSystemController

from simulation.file_io.csv_saver import CSVSaver
from uuid import uuid4


class SimulationEngine:
    def __init__(self, traffic_system: TrafficSystem):
        self.traffic_system = traffic_system
        self.traffic_control = TrafficSystemController(self.traffic_system)
        self.csv_saver = CSVSaver(uuid4())

    def update_movement(self):
        self.traffic_control.move_all_vehicles()

    def update_lights(self):
        self.traffic_control.update_traffic_lights()

    def generate_vehicles(self):
        for _ in range(self.traffic_system.config.vehicles_per_second):
            self.traffic_system.generate_random_car()

    def save_stats(self, time: float):
        for intersection in self.traffic_system.intersections.values():

            self.csv_saver.save(intersection.id,
                                time,
                                intersection.vehicles_passed,
                                self.traffic_system.config.intersection_type,
                                self.traffic_system.config.lights_switch_strategy,
                                self.traffic_system.config.light_duration,
                                self.traffic_system.config.vehicles_per_second)
