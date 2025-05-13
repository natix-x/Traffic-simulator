from abc import ABCMeta, abstractmethod

from domain.entities import Vehicle


class PriorityRulesInterface(metaclass=ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'should_give_way') and
                callable(subclass.should_give_way) or
                NotImplemented)

    @abstractmethod
    def set_context(self, **kwargs):
        """ Sets the contextual data needed to evaluate the situation
    (e.g., vehicle position, traffic lights, road signs)."""
        raise NotImplementedError

    @abstractmethod
    def should_give_way(self, vehicle: Vehicle) -> bool:
        raise NotImplementedError
