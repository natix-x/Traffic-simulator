import operator
from typing import TYPE_CHECKING

from simulation.domain.models import Position
from simulation.domain.services.lights_switching_strategies.most_cars_green import MostCarsGreen

if TYPE_CHECKING:
    from simulation.domain.aggregates.traffic_system import TrafficSystem


class MostCarsGreenBasic(MostCarsGreen):
    def __init__(self, traffic_system: "TrafficSystem"):
        super().__init__(traffic_system)

    def choose_next_green_position(self) -> Position:
        super().count_vehicles_waiting_on_each_lane()
        return max(self.waiting_number.items(), key=operator.itemgetter(1))[0]
