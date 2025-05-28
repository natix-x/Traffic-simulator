import random
from typing import TYPE_CHECKING

from domain.entities import TrafficLight
from domain.models import Position, TrafficLightState

if TYPE_CHECKING:
    from domain.aggregates.traffic_system import TrafficSystem


class SingleDirectionGreen:
    @staticmethod
    def initial_traffic_lights_setup():
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

    @staticmethod
    def update_traffic_lights(traffic_system: "TrafficSystem"):
        green_found = False
        lights = list(traffic_system.traffic_lights.values())
        for i, light in enumerate(lights):
            light.state_timer += 1
            if light.state == TrafficLightState.GREEN and light.state_timer >= 5:
                light.change_state(TrafficLightState.RED)
                next_index = (i + 1) % len(lights)
                green_found = True
                break

        if green_found:
            lights[next_index].change_state(TrafficLightState.GREEN)
