import time

from domain.aggregates.traffic_system import TrafficSystem
from domain.entities import TrafficLight
from domain.models import Position, TrafficLightState
from domain.service.traffic_control import TrafficControl


class SimulationEngine:
    def __init__(self, traffic_system: TrafficSystem, tick_duration: float = 1.0):
        self.traffic_system = traffic_system
        self.tick_duration = tick_duration
        self.traffic_control = TrafficControl(self.traffic_system)

    def run(self, ticks: int = 10):
        self._initial_traffic_lights_setup()

        for tick in range(ticks):
            print(f"\n=== Tick {tick + 1} ===")

            self.traffic_control.update_traffic_lights()

            for i in range(2):  # generowanie w każdej klatce symulacji 2 pojazdów, TODO: updatowanie przez użytkownika
                self.traffic_system.generate_random_car()

            self.traffic_control.move_all_vehicles()

            self._log_state()  # helper function

            time.sleep(self.tick_duration)

    def _initial_traffic_lights_setup(self):
        for inter in self.traffic_system.intersections:
            for pos in list(Position):
                self.traffic_system.add_traffic_light(TrafficLight(
                    state=TrafficLightState.RED,
                    intersection=self.traffic_system.intersections[inter],
                    position=pos
                ))

    def _log_state(self):
        for vehicle in self.traffic_system.vehicles.values():
            position = vehicle.current_position if vehicle.current_position else "None"
            print(f"Vehicle {vehicle.id} is at intersection {position}, direction: {vehicle.direction}")

        for light in self.traffic_system.traffic_lights.values():
            print(f"Traffic light {light.id} is {light.state}")
