import pygame

from domain.entities import Vehicle


class VehicleRender:
    def __init__(self, vehicle: Vehicle, image: pygame.surface, screen: pygame.surface):
        self.vehicle = vehicle
        self.screen = screen

    # def render(self):
    #     self.screen.blit(self.vehicle.image, (self.vehicle.x, self.vehicle.y))

    def update(self):
        self.vehicle.move()


        # state = self.vehicle.current_state
        # position = self.vehicle.current_position
        #
        # self._go_forward(position)
        #
        # if state == VehicleState.APPROACH:
        #     if position == Position.S:
        #         if self.y <= 300:
        #             self.vehicle.current_state = VehicleState.IN_INTERSECTION
        #             self.vehicle.move()
        #     elif position == Position.N:
        #         if self.y >= 200:
        #             self.vehicle.current_state = VehicleState.IN_INTERSECTION
        #             self.vehicle.move()
        #     elif position == Position.E:
        #         if self.x <= 300:
        #             self.vehicle.current_state = VehicleState.IN_INTERSECTION
        #             self.vehicle.move()
        #     elif position == Position.W:
        #         if self.x >= 200:
        #             self.vehicle.current_state = VehicleState.IN_INTERSECTION
        #             self.vehicle.move()

    # # TODO: nie zardcodować wartości - obliczać dynamicznie, dodać logikę jak więcej skrzyżowań
    # def _calculate_initial_coordinates(self):
    #     position = self.vehicle.current_position
    #     if position == Position.S:
    #         return 290, 500
    #     elif position == Position.N:
    #         return 210, 6
    #     elif position == Position.E:
    #         return 490, 220
    #     elif position == Position.W:
    #         return 0, 290

    # def _go_forward(self, position: Position):
    #     if position == Position.S:
    #         self.y -= 2 #self.vehicle.speed
    #     elif position == Position.N:
    #         self.y += 2 #self.vehicle.speed
    #     elif position == Position.E:
    #         self.x -= 2 #self.vehicle.speed
    #     elif position == Position.W:
    #         self.x += 2 #self.vehicle.speed



