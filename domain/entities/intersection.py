from dataclasses import dataclass


@dataclass
class Intersection:
    id: str
    connected_roads: list[str]


def intersection_factory(id: str, connected_roads: list[str]) -> Intersection:
    return Intersection(id=id, connected_roads=connected_roads)