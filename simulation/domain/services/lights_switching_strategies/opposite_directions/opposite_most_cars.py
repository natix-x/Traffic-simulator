from typing import TYPE_CHECKING

from simulation.domain.services.lights_switching_strategies.opposite_most_cars_green import OppositeMostCarsGreen
from simulation.domain.services.lights_switching_strategies.single_direction.single_most_cars import SingleMostCars

if TYPE_CHECKING:
    from simulation.domain.entities import TrafficLightsIntersection


class OppositeMostCars(SingleMostCars, OppositeMostCarsGreen):
    def __init__(self, intersection: "TrafficLightsIntersection"):
        super().__init__(intersection)

    def initial_traffic_lights_setup(self):
        return OppositeMostCarsGreen.initial_traffic_lights_setup()

    def update_traffic_lights(self):
        OppositeMostCarsGreen.update_traffic_lights(self)
