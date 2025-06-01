from domain.services.lights_switching_strategies.lights_switch_strategy import LightsSwitchStrategy


class MaxWaitFirst(LightsSwitchStrategy):


    @staticmethod
    def initial_traffic_lights_setup() -> list[TrafficLight]:
        ...

    def