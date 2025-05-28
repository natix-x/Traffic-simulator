from domain.entities import Intersection
from domain.services.priority.priority_rules import PriorityRules


class TrafficSignsIntersectionRule(PriorityRules):
    def set_context(self, intersection: Intersection):
        pass

    def should_give_way(self) -> bool:
        return False
