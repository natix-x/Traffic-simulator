import os
import threading

import pygame
from pygame.locals import *

from application.simulation_engine import SimulationEngine
from domain.aggregates.traffic_system import TrafficSystem
from domain.entities import Intersection
from ui.renders.vehicle_render import VehicleRender


class SimulationScreen:
    def __init__(self, screen):
        self.running = True
        self.screen = screen
        self.background = pygame.transform.scale(
            pygame.image.load(os.path.join("ui", "resources", "images", "intersection.png")), (512, 512)
        )
        self.traffic_system = TrafficSystem()
        intersection = Intersection()
        self.traffic_system.add_intersection(intersection)
        self.engine = SimulationEngine(self.traffic_system, tick_duration=1.0)
        self.vehicle_renders = []
        self.vehicle_image = pygame.Surface((20, 10))
        self.vehicle_image.fill((255, 0, 0))
        self._start_simulation()

    def _start_simulation(self):
        simulation_thread = threading.Thread(
            target=self._run_simulation_logic, daemon=True
        )
        simulation_thread.start()
        pygame.display.set_caption("Simulation")
        while self.running:
            self.screen.blit(self.background, (0, 0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False

            for vehicle in self.traffic_system.vehicles.values():
                if vehicle.current_position:
                    vehicle_render = VehicleRender(vehicle, self.vehicle_image, self.screen)
                    vehicle_render.render()

            pygame.display.update()
        pygame.quit()

    def _run_simulation_logic(self):
        self.engine.run(ticks=20)


