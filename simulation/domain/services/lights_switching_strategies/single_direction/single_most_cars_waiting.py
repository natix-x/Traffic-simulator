import operator
from typing import TYPE_CHECKING

from simulation.domain.models import Position, VehicleState
from simulation.domain.services.lights_switching_strategies.single_most_cars_green import SingleMostCarsGreen

if TYPE_CHECKING:
    from simulation.domain.entities import TrafficLightsIntersection


class SingleMostCarsWaiting(SingleMostCarsGreen):
    def __init__(self, intersection: "TrafficLightsIntersection"):
        super().__init__(intersection)

        self.max_waiting_per_position: dict[Position, int] = {}

    def choose_next_green_position(self):
        super().count_vehicles_waiting_on_each_lane()
        self._update_waiting_times()
        score_map = {
            pos: self.waiting_number[pos] * 3 + self.max_waiting_per_position[pos]
            for pos in self.max_waiting_per_position
        }
        return max(score_map.items(), key=operator.itemgetter(1))[0]

    def _update_waiting_times(self):
        self.max_waiting_per_position = {}

        for vehicle_list in self.intersection.vehicles.values():
            for vehicle in vehicle_list:
                if vehicle.current_state in [VehicleState.AT_STOP_LINE, VehicleState.APPROACH]:
                    pos = vehicle.current_position
                    wait_time = vehicle.waiting_time
                    if pos not in self.max_waiting_per_position:
                        self.max_waiting_per_position[pos] = wait_time
                    else:
                        self.max_waiting_per_position[pos] = max(self.max_waiting_per_position[pos], wait_time)
