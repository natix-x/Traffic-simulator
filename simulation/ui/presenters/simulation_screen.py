import os

import pygame
from pygame.locals import *

from simulation.application.simulation_engine import SimulationEngine
from simulation.config import AppConfig, SimulationConfig
from simulation.domain.aggregates.traffic_system import TrafficSystem
from simulation.ui.renders.traffic_light_render import TrafficLightRender
from simulation.ui.renders.vehicle_render import VehicleRender


class SimulationScreen:
    def __init__(self, screen, configuration: SimulationConfig):

        self.running = True
        self.screen = screen
        self.background = pygame.transform.scale(
            pygame.image.load(os.path.join("simulation", "ui", "resources", "images", "intersection.png")),
            (AppConfig.WIDTH, AppConfig.HEIGHT)
        )

        self.traffic_system = TrafficSystem(configuration)
        self.engine = SimulationEngine(self.traffic_system)

        self.traffic_lights_renders = {}

        self.vehicle_renders = {}
        self.vehicle_image = pygame.Surface((20, 10))
        self.vehicle_image.fill(AppConfig.RED)

        pygame.display.set_caption("Simulation")
        self._run()

    def _run(self):
        clock = pygame.time.Clock()
        last_update = 0

        while self.running:
            self.screen.blit(self.background, (0, 0))

            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False

            current_time = pygame.time.get_ticks()

            if current_time - last_update >= 1000:
                self.engine.update_lights()
                self.engine.generate_vehicles()
                self.engine.save_stats(time=current_time)
                last_update = current_time

            self.engine.update_movement()

            self._update_vehicle_renders()
            self._update_traffic_lights_renders()

            for vehicle_render in self.vehicle_renders.values():
                vehicle_render.render()

            for light_render in self.traffic_lights_renders.values():
                light_render.render()

            pygame.display.update()
            clock.tick(AppConfig.FPS)

        pygame.quit()

    def _update_vehicle_renders(self):
        for vehicle in self.traffic_system.vehicles.values():
            if vehicle.id not in self.vehicle_renders:
                self.vehicle_renders[vehicle.id] = VehicleRender(vehicle, self.vehicle_image, self.screen)

    def _update_traffic_lights_renders(self):
        for traffic_light in self.traffic_system.traffic_lights.values():
            if traffic_light.id not in self.traffic_lights_renders:
                self.traffic_lights_renders[traffic_light.id] = TrafficLightRender(traffic_light,
                                                                                   self.screen)