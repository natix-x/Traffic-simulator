from enum import Enum


class IntersectionType(Enum):
    TRAFFIC_LIGHTS_INTERSECTION = "TRAFFIC_LIGHTS_INTERSECTION"
    EQUAL_INTERSECTION = "EQUAL_INTERSECTION"
    TRAFFIC_SIGNS_INTERSECTION = "TRAFFIC_SIGNS_INTERSECTION"

    def __str__(self):
        return self.value
