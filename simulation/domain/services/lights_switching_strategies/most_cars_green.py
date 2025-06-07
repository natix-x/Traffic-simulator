from collections import defaultdict

from simulation.domain.entities import TrafficLight
from simulation.domain.models import VehicleState
from simulation.domain.services.lights_switching_strategies.lights_switch_strategy import LightsSwitchStrategy
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from simulation.domain.entities import TrafficLight, TrafficLightsIntersection


class MostCarsGreen(LightsSwitchStrategy):
    def __init__(self, intersection: "TrafficLightsIntersection"):
        super().__init__(intersection)
        self.waiting_number = defaultdict(int)

    @staticmethod
    def initial_traffic_lights_setup() -> list[TrafficLight]:
        raise NotImplementedError

    def update_traffic_lights(self):
        raise NotImplementedError

    def count_vehicles_waiting_on_each_lane(self):
        self.waiting_number = defaultdict(int)

        for vehicle_list in self.intersection.vehicles.values():
            for vehicle in vehicle_list:
                if vehicle.current_state in [VehicleState.AT_STOP_LINE, VehicleState.APPROACH]:
                    self.waiting_number[vehicle.current_position] += 1

