from domain.aggregates.traffic_system import TrafficSystem
from domain.entities import TrafficLight
from domain.models import Position, TrafficLightState
from domain.services.traffic_control import TrafficControl


# TODO: dostosować do nowych zasad ruchu
class SimulationEngine:
    def __init__(self, traffic_system: TrafficSystem):
        self.traffic_system = traffic_system
        self._initial_traffic_lights_setup()
        self.traffic_control = TrafficControl(self.traffic_system)

    def update_movement(self):
        self.traffic_control.move_all_vehicles()

    def update_lights(self):
        self.traffic_control.update_traffic_lights()

    def generate_vehicles(self):
        for _ in range(2):  # Możesz to dostosować
            self.traffic_system.generate_random_car()

    def _initial_traffic_lights_setup(self):
        for inter in self.traffic_system.intersections:
            for pos in list(Position):
                if pos in [Position.N, Position.S]:
                    self.traffic_system.add_traffic_light(TrafficLight(
                        state=TrafficLightState.GREEN,
                        intersection=self.traffic_system.intersections[inter],
                        position=pos
                    ))
                else:
                    self.traffic_system.add_traffic_light(TrafficLight(
                        state=TrafficLightState.RED,
                        intersection=self.traffic_system.intersections[inter],
                        position=pos
                    ))
