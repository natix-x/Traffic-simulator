import random
import operator
from typing import TYPE_CHECKING
from collections import defaultdict

from domain.models import Position, TrafficLightState, VehicleState
from domain.services.lights_switching_strategies.single_direction_green import SingleDirectionGreen

if TYPE_CHECKING:
    from domain.aggregates.traffic_system import TrafficSystem


class MaxWaitGreen(SingleDirectionGreen):
    def __init__(self, traffic_system: "TrafficSystem"):
        super().__init__(traffic_system)
        self.waiting_time: dict[Position, int] = defaultdict(int)

    def update_traffic_lights(self):
        green_found = False
        lights = list(self.traffic_system.traffic_lights.values())

        for light in lights:
            light.state_timer += 1
            if light.state == TrafficLightState.GREEN and light.state_timer >= self.traffic_system.config.light_duration:
                light.change_state(TrafficLightState.RED)
                green_found = True
                break

        if green_found:
            self._count_waiting_vehicles_time()
            if self.waiting_time:
                pos = max(self.waiting_time.items(), key=operator.itemgetter(1))[0]
            else:
                pos = random.choice(list(Position))

            for traffic_light in self.traffic_system.traffic_lights.values():
                if traffic_light.position == pos:
                    traffic_light.change_state(TrafficLightState.GREEN)
                    self.waiting_time[pos] = 0

    def _count_waiting_vehicles_time(self):
        waiting_number = defaultdict(int)

        for vehicle in self.traffic_system.vehicles.values():
            if vehicle.current_state in [VehicleState.AT_STOP_LINE, VehicleState.APPROACH]:
                waiting_number[vehicle.current_position] += 1

        for pos in Position:
            if pos in waiting_number and waiting_number[pos] > 0:
                self.waiting_time[pos] += 1
            else:
                self.waiting_time[pos] = 0
