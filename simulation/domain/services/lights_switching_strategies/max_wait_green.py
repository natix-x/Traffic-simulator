import random
import operator
from typing import TYPE_CHECKING
from collections import defaultdict

from simulation.domain.models import Position, TrafficLightState, VehicleState
from simulation.domain.services.lights_switching_strategies.single_direction_green import SingleDirectionGreen

if TYPE_CHECKING:
    from simulation.domain.aggregates.traffic_system import TrafficSystem


class MaxWaitGreen(SingleDirectionGreen):
    def __init__(self, traffic_system: "TrafficSystem"):
        super().__init__(traffic_system)
        self.waiting_time: dict[Position, int] = defaultdict(int)

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
            pos = self._find_position_with_longest_waiting_vehicle()
            for traffic_light in self.traffic_system.traffic_lights.values():
                if traffic_light.position == pos and traffic_light.state == TrafficLightState.RED:
                    traffic_light.change_state(TrafficLightState.GREEN)
                    self.waiting_time[pos] = 0

    def _find_position_with_longest_waiting_vehicle(self):
        max_waiting_per_position = {}

        for vehicle in self.traffic_system.vehicles.values():
            if vehicle.current_state in [VehicleState.AT_STOP_LINE, VehicleState.APPROACH]:
                pos = vehicle.current_position
                wait_time = vehicle.waiting_time
                if pos not in max_waiting_per_position:
                    max_waiting_per_position[pos] = wait_time
                else:
                    max_waiting_per_position[pos] = max(max_waiting_per_position[pos], wait_time)

        if max_waiting_per_position:
            pos = max(max_waiting_per_position.items(), key=operator.itemgetter(1))[0]
        else:
            pos = random.choice(list(Position))

        return pos
