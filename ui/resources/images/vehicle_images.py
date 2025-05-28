import pygame

from domain.models import VehicleType, Position

# Rozmiary (możesz dostosować)
SIZE = {
    VehicleType.CAR: (30, 15),
    VehicleType.BUS: (35, 15),
    VehicleType.TRACK: (40, 15),
    VehicleType.BIKE: (20, 10)
}


def load_vehicle_image(path: str, width: int, height: int):
    return pygame.transform.scale(
        pygame.image.load(f"./ui/resources/images/{path}"), (width, height)
    )


# CARS
CAR_N = load_vehicle_image("cars/car_N.png", 15, 30)
CAR_S = load_vehicle_image("cars/car_S.png", 15, 30)
CAR_E = load_vehicle_image("cars/car_E.png", 30, 15)
CAR_W = load_vehicle_image("cars/car_W.png", 30, 15)

# BUSES
BUS_N = load_vehicle_image("buses/bus_N.png", 15, 30)
BUS_S = load_vehicle_image("buses/bus_S.png", 15, 30)
BUS_E = load_vehicle_image("buses/bus_E.png", 30, 15)
BUS_W = load_vehicle_image("buses/bus_W.png", 30, 15)

# TRUCKS
TRACK_N = load_vehicle_image("tracks/track_N.png", 15, 30)
TRACK_S = load_vehicle_image("tracks/track_S.png", 15, 30)
TRACK_E = load_vehicle_image("tracks/track_E.png", 30, 15)
TRACK_W = load_vehicle_image("tracks/track_W.png", 30, 15)

# BIKES
BIKE_N = load_vehicle_image("bikes/bike_N.png", 10, 20)
BIKE_S = load_vehicle_image("bikes/bike_S.png", 10, 20)
BIKE_E = load_vehicle_image("bikes/bike_E.png", 20, 10)
BIKE_W = load_vehicle_image("bikes/bike_W.png", 20, 10)

# PRIORITY - POLICE
POLICE_N = load_vehicle_image("polices/police_N.png", 40, 30)
POLICE_S = load_vehicle_image("polices/police_S.png", 40, 30)
POLICE_E = load_vehicle_image("polices/police_E.png", 30, 40)
POLICE_W = load_vehicle_image("polices/police_W.png", 30, 40)

# Vehicles dict
VEHICLE_IMAGES = {
    Position.S: {
        VehicleType.CAR: CAR_N,
        VehicleType.BUS: BUS_N,
        VehicleType.TRACK: TRACK_N,
        VehicleType.BIKE: BIKE_N,
        VehicleType.POLICE: POLICE_N
    },
    Position.N: {
        VehicleType.CAR: CAR_S,
        VehicleType.BUS: BUS_S,
        VehicleType.TRACK: TRACK_S,
        VehicleType.BIKE: BIKE_S,
        VehicleType.POLICE: POLICE_S
    },
    Position.W: {
        VehicleType.CAR: CAR_E,
        VehicleType.BUS: BUS_E,
        VehicleType.TRACK: TRACK_E,
        VehicleType.BIKE: BIKE_E,
        VehicleType.POLICE: POLICE_E
    },
    Position.E: {
        VehicleType.CAR: CAR_W,
        VehicleType.BUS: BUS_W,
        VehicleType.TRACK: TRACK_W,
        VehicleType.BIKE: BIKE_W,
        VehicleType.POLICE: POLICE_W
    },
}
