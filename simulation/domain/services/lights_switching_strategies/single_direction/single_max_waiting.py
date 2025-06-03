import operator
from collections import defaultdict
from typing import TYPE_CHECKING

from simulation.domain.models import Position, VehicleState
from simulation.domain.services.lights_switching_strategies.single_most_cars_green import SingleMostCarsGreen

if TYPE_CHECKING:
    from simulation.domain.entities import TrafficLightsIntersection


class SingleMaxWaiting(SingleMostCarsGreen):
    def __init__(self, intersection: "TrafficLightsIntersection"):
        super().__init__(intersection)
        self.waiting_time: dict[Position, int] = defaultdict(int)

    def choose_next_green_position(self) -> Position:
        max_waiting_per_position = {}

        for vehicle_list in self.intersection.vehicles.values():
            for vehicle in vehicle_list:
                if vehicle.current_state in [VehicleState.AT_STOP_LINE, VehicleState.APPROACH]:
                    pos = vehicle.current_position
                    wait_time = vehicle.waiting_time
                    if pos not in max_waiting_per_position:
                        max_waiting_per_position[pos] = wait_time
                    else:
                        max_waiting_per_position[pos] = max(max_waiting_per_position[pos], wait_time)

        if max_waiting_per_position:
            return max(max_waiting_per_position.items(), key=operator.itemgetter(1))[0]
