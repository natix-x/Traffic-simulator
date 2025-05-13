from domain.entities import Intersection
from domain.services.priority.priority_rules_interface import PriorityRulesInterface


class TrafficSignsIntersectionRule(PriorityRulesInterface):
    def set_context(self, intersection: Intersection):
        pass

    def should_give_way(self) -> bool:
        return False
