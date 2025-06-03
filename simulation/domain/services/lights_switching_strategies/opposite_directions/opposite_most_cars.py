from typing import TYPE_CHECKING

from simulation.domain.services.lights_switching_strategies.opposite_most_cars_green import OppositeMostCarsGreen
from simulation.domain.services.lights_switching_strategies.single_direction.single_most_cars import SingleMostCars

if TYPE_CHECKING:
    from simulation.domain.aggregates.traffic_system import TrafficSystem


class OppositeMostCars(SingleMostCars, OppositeMostCarsGreen):
    def __init__(self, traffic_system: "TrafficSystem"):
        super().__init__(traffic_system)
