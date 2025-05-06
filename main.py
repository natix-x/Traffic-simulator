from application.simulation_engine import SimulationEngine
from domain.aggregates.traffic_system import TrafficSystem
from domain.entities import Intersection, TrafficLight, Vehicle
from domain.models import TrafficLightState, VehicleDirection, VehicleType

intersection = Intersection()
light = TrafficLight(state=TrafficLightState.RED, intersection=intersection)


traffic_system = TrafficSystem(intersections={}, traffic_lights={}, vehicles={})
traffic_system.add_intersection(intersection)
traffic_system.add_traffic_light(light)


simulation_engine = SimulationEngine(traffic_system, tick_duration=1.0)
simulation_engine.run(ticks=10)
