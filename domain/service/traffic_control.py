from domain.aggregates.traffic_system import TrafficSystem
from domain.models import TrafficLightState
from domain.entities import Vehicle


class TrafficControl:
    def __init__(self, traffic_system: TrafficSystem):
        self.traffic_system = traffic_system

    def update_traffic_lights(self):  # poprawa logiki działania świateł w symulacji, początkowo jedne światła na raz mogą być zielone
        for light in self.traffic_system.traffic_lights.values():
            if light.state == TrafficLightState.RED:
                light.change_state(TrafficLightState.GREEN)
            elif light.state == TrafficLightState.GREEN:
                light.change_state(TrafficLightState.YELLOW)
            elif light.state == TrafficLightState.YELLOW:
                light.change_state(TrafficLightState.RED)

    def move_all_vehicles(self):
        for vehicle_id in self.traffic_system.vehicles:
            vehicle = self.traffic_system.vehicles[vehicle_id]

            if self.can_vehicle_move(vehicle):
                self.traffic_system.move_vehicle(vehicle_id)

    def can_vehicle_move(self, vehicle: Vehicle) -> bool:
        current_vehicle_intersection = vehicle.current_intersection
        current_vehicle_position = vehicle.current_position
        for traffic_light_id in self.traffic_system.traffic_lights:
            current_light = self.traffic_system.traffic_lights[traffic_light_id]
            if current_light.intersection == current_vehicle_intersection and current_light.position == current_vehicle_position:
                break
        return current_light.state == TrafficLightState.GREEN  # TODO: dodać osługę błędów

