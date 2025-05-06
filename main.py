from domain.entities import Intersection, TrafficLight, Vehicle
from domain.models import TrafficLightState, Direction, VehicleType
from application.simulation_engine import SimulationEngine
from domain.aggregates.traffic_system import TrafficSystem


intersection = Intersection(id="A")
light = TrafficLight(id="L1", state=TrafficLightState.RED, intersection=intersection)


traffic_system = TrafficSystem(intersections={}, traffic_lights={}, vehicles={})
traffic_system.add_intersection(intersection)
traffic_system.add_traffic_light(light)
traffic_system.add_vehicle(vehicle1)
traffic_system.add_vehicle(vehicle2)


simulation_engine = SimulationEngine(traffic_system, tick_duration=1.0)
simulation_engine.run(ticks=10)
