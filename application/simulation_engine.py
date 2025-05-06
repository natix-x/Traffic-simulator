import time

from domain.aggregates.traffic_system import TrafficSystem
from domain.service.traffic_control import update_traffic_lights


# TODO: poprawa logiki
class SimulationEngine:
    def __init__(self, traffic_system: TrafficSystem, tick_duration: float = 1.0):
        self.traffic_system = traffic_system
        self.tick_duration = tick_duration

    def run(self, ticks: int = 10):
        for tick in range(ticks):
            print(f"\n=== Tick {tick + 1} ===")

            update_traffic_lights(self.traffic_system)

            for i in range(2): # generowanie w każdej klatce 2 pojazdów
                self.traffic_system.generate_random_car()

            self._move_vehicles()

            # usuwanie z symulacji samochodów, które przejechały już skrzyżowanie, może w GUI?

            self._log_state()

            time.sleep(self.tick_duration)

    def _move_vehicles(self):
        for vehicle_id in list(self.traffic_system.vehicles.keys()):
            self.traffic_system.move_vehicle(vehicle_id)  # na pewno do usunięcia później bo tutaj nie pasuje
            # poruszać nie wszystkie samochody w jednym ruchu, tylko te co mają zielone światło

    def _log_state(self):
        for vehicle in self.traffic_system.vehicles.values():
            position = vehicle.current_position if vehicle.current_position else "None"
            print(f"Vehicle {vehicle.id} is at intersection {position}, direction: {vehicle.direction}")

        for light in self.traffic_system.traffic_lights.values():
            print(f"Traffic light {light.id} is {light.state}")
