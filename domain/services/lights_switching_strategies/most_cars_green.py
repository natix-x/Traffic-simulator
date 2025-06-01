import random
import operator
from typing import TYPE_CHECKING
from collections import defaultdict

from domain.entities import TrafficLight
from domain.models import Position, TrafficLightState, VehicleState
from domain.services.lights_switching_strategies.lights_switch_strategy import LightsSwitchStrategy

if TYPE_CHECKING:
    from domain.aggregates.traffic_system import TrafficSystem


class MostCarsGreen(LightsSwitchStrategy):
    def __init__(self, traffic_system: "TrafficSystem"):
        super().__init__(traffic_system)

    def initial_traffic_lights_setup(self):
        rand_position = random.choice([Position.N, Position.S, Position.E, Position.W])
        lights = []

        for pos in list(Position):
            if pos == rand_position:
                lights.append(TrafficLight(
                    state=TrafficLightState.GREEN,
                    position=pos
                ))
            else:
                lights.append(TrafficLight(
                    state=TrafficLightState.RED,
                    position=pos
                ))

        return lights

    def update_traffic_lights(self):
        green_found = False
        lights = list(self.traffic_system.traffic_lights.values())
        for i, light in enumerate(lights):
            light.state_timer += 1
            if light.state == TrafficLightState.GREEN and light.state_timer >= self.traffic_system.config.light_duration:
                light.change_state(TrafficLightState.RED)
                green_found = True
                break

        if green_found:
            self.count_vehicles_waiting_on_each_lane()
            if self.waiting_vehicles:
                pos = max(self.waiting_vehicles.items(), key=operator.itemgetter(1))[0]
            else:
                pos = random.choice(list(Position))
            for traffic_light in self.traffic_system.traffic_lights.values():
                if traffic_light.position == pos:
                    traffic_light.change_state(TrafficLightState.GREEN)

    def count_vehicles_waiting_on_each_lane(self):
        self.waiting_vehicles = defaultdict(int)
        for vehicle in self.traffic_system.vehicles.values():
            if vehicle.current_state in [VehicleState.AT_STOP_LINE, VehicleState.APPROACH]:
                self.waiting_vehicles[vehicle.current_position] += 1
