import os
import threading

import pygame
from pygame.locals import *

from application.simulation_engine import SimulationEngine
from config import AppConfig
from domain.aggregates.traffic_system import TrafficSystem
from domain.entities import Intersection
from ui.renders.traffic_light_render import TrafficLightRender
from ui.renders.vehicle_render import VehicleRender


class SimulationScreen:
    def __init__(self, screen):

        self.running = True
        self.screen = screen
        self.background = pygame.transform.scale(
            pygame.image.load(os.path.join("ui", "resources", "images", "intersection.png")), AppConfig.WINDOW_SIZE
        )

        self.traffic_system = TrafficSystem()
        self.traffic_system.add_intersection(Intersection())
        self.engine = SimulationEngine(self.traffic_system, tick_duration=1.0)

        self.traffic_lights_renders = {}

        self.vehicle_renders = {}
        self.vehicle_image = pygame.Surface((20, 10))
        self.vehicle_image.fill(AppConfig.RED)
        self._start_simulation()
        self._run()

    def _start_simulation(self):
        simulation_thread = threading.Thread(
            target=lambda: self.engine.run(ticks=100), daemon=True
        )
        simulation_thread.start()
        pygame.display.set_caption("Simulation")

    def _run(self):
        clock = pygame.time.Clock()
        while self.running:
            self.screen.blit(self.background, (0, 0))

            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False

            self._update_vehicle_renders()
            self._update_traffic_lights_renders()

            for vehicle_render in self.vehicle_renders.values():
                vehicle_render.update()
                vehicle_render.render()

            for light_render in self.traffic_lights_renders.values():
                light_render.render()

            pygame.display.update()
            clock.tick(30)

        pygame.quit()

    def _update_vehicle_renders(self):
        for vehicle in self.traffic_system.vehicles.values():
            if vehicle.id not in self.vehicle_renders:
                self.vehicle_renders[vehicle.id] = VehicleRender(vehicle, self.vehicle_image, self.screen)

    def _update_traffic_lights_renders(self):
        for traffic_light in self.traffic_system.traffic_lights.values():
            if traffic_light.id not in self.vehicle_renders:
                self.traffic_lights_renders[traffic_light.id] = TrafficLightRender(traffic_light,
                                                                                   self.screen)
