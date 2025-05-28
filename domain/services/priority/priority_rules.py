import math
from abc import ABCMeta, abstractmethod
from typing import TYPE_CHECKING

from domain.models import Position

if TYPE_CHECKING:
    from domain.entities.vehicle import Vehicle


class PriorityRules(metaclass=ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'should_give_way') and
                callable(subclass.should_give_way) or
                NotImplemented)

    def set_context(self, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def should_give_way(self, vehicle: "Vehicle") -> bool:
        raise NotImplementedError

    @staticmethod
    def get_right_position(vehicle: "Vehicle") -> Position:
        return {
            Position.N: Position.W,
            Position.E: Position.N,
            Position.S: Position.E,
            Position.W: Position.S,
        }[vehicle.current_position]

    @staticmethod
    def distance_between(v1: "Vehicle", v2: "Vehicle") -> float:
        dx = v1.x - v2.x
        dy = v1.y - v2.y
        return math.sqrt(dx * dx + dy * dy)
