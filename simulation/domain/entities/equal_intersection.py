from simulation.domain.entities import Intersection
from simulation.domain.services.priority.equal_intersection_rule import EqualIntersectionRule


class EqualIntersection(Intersection):
    def __init__(self):
        super().__init__()
        self.add_priority_rules()

    def add_priority_rules(self):
        priority_rule = EqualIntersectionRule()
        priority_rule.set_context(intersection=self)
        self.priority_rule = priority_rule
