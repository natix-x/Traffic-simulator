from dataclasses import dataclass
from domain.entities.intersection import Intersection


@dataclass
class Vehicle:
    id: str
    type: str
    speed: int
    current_route: list[Intersection]
    current_position: Intersection | None = None


def vehicle_factory(
    id: str, type: str, speed: int, current_route: list[Intersection], current_position: Intersection | None = None
) -> Vehicle:
    return Vehicle(id=id, type=type, speed=speed, current_route=current_route, current_position=current_position)