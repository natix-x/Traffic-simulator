import operator
from typing import TYPE_CHECKING

from simulation.domain.models import Position
from simulation.domain.services.lights_switching_strategies.single_most_cars_green import SingleMostCarsGreen

if TYPE_CHECKING:
    from simulation.domain.entities import TrafficLightsIntersection


class SingleMostCars(SingleMostCarsGreen):
    def __init__(self, intersection: "TrafficLightsIntersection"):
        super().__init__(intersection)

    def choose_next_green_position(self) -> Position:
        super().count_vehicles_waiting_on_each_lane()
        return max(self.waiting_number.items(), key=operator.itemgetter(1))[0]
