import time
from domain.aggregates.traffic_system import TrafficSystem
from domain.models import TrafficLightState, VehicleType, Direction
from domain.entities import Vehicle


class SimulationEngine:  # TODO: wyczeszczenie tej klasy, przeniesienie części metod do service
    def __init__(self, traffic_system: TrafficSystem, tick_duration: float = 1.0):
        self.traffic_system = traffic_system
        self.tick_duration = tick_duration

    def run(self, ticks: int = 10):
        for tick in range(ticks):
            print(f"\n=== Tick {tick + 1} ===")

            self._update_traffic_lights()

            self._move_vehicles()

            self._log_state()

            time.sleep(self.tick_duration)

    def _update_traffic_lights(self):
        for light in self.traffic_system.traffic_lights.values():
            if light.state == TrafficLightState.RED:
                light.change_state(TrafficLightState.GREEN)
            elif light.state == TrafficLightState.GREEN:
                light.change_state(TrafficLightState.YELLOW)
            elif light.state == TrafficLightState.YELLOW:
                light.change_state(TrafficLightState.RED)

    def _move_vehicles(self):
        for vehicle_id in list(self.traffic_system.vehicles.keys()):
            self.traffic_system.move_vehicle(vehicle_id)

    def _log_state(self):
        for vehicle in self.traffic_system.vehicles.values():
            position = vehicle.current_position.id if vehicle.current_position else "None"
            print(f"Vehicle {vehicle.id} is at intersection {position}, direction: {vehicle.direction}")

        for light in self.traffic_system.traffic_lights.values():
            print(f"Traffic light {light.id} is {light.state}")

