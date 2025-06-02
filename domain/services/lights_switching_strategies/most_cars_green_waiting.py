import operator
from typing import TYPE_CHECKING
from collections import defaultdict

from domain.models import Position, VehicleState
from domain.services.lights_switching_strategies.most_cars_green import MostCarsGreen
from domain.services.lights_switching_strategies.single_direction_green import SingleDirectionGreen

if TYPE_CHECKING:
    from domain.aggregates.traffic_system import TrafficSystem


class MostCarsGreenWaiting(MostCarsGreen):
    def __init__(self, traffic_system: "TrafficSystem"):
        super().__init__(traffic_system)
        self.waiting_time: dict[Position, int] = defaultdict(int)

    def choose_next_green_position(self):
        super().count_vehicles_waiting_on_each_lane()
        self._count_waiting_vehicle_time()
        score_map = {
            pos: self.waiting_number[pos] * 3 + self.waiting_time[pos]
            for pos in self.waiting_time
        }
        return max(self.waiting_time.items(), key=operator.itemgetter(1))[0]

    def _count_waiting_vehicle_time(self):
        for pos in Position:
            if pos in self.waiting_number and self.waiting_number[pos] > 0:
                self.waiting_time[pos] += 1
            else:
                self.waiting_time[pos] = 0
