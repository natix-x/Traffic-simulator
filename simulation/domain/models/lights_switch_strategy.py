from enum import Enum


class LightsSwitchStrategy(Enum):

    # basic
    SINGLE_FIXED_CYCLE = "SINGLE_FIXED_CYCLE"
    OPPOSITE_FIXED_CYCLE = "OPPOSITE_FIXED_CYCLE"

    # most cars - basic version
    SINGLE_MOST_CARS = "SINGLE_MOST_CARS"
    OPPOSITE_MOST_CARS = "OPPOSITE_MOST_CARS"

    # most cars + waiting time
    SINGLE_MOST_CARS_WAITING = "SINGLE_MOST_CARS_WAITING"
    OPPOSITE_MOST_CARS_WAITING = "OPPOSITE_MOST_CARS_WAITING"

    # max waiting time
    SINGLE_MAX_WAIT = "SINGLE_MAX_WAIT"
    OPPOSITE_MAX_WAIT = "OPPOSITE_MAX_WAIT"

    def __str__(self):
        return self.value
