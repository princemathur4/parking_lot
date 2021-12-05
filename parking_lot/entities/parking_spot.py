from abc import ABCMeta, abstractmethod
from parking_lot.entities.vehicle import Vehicle
from parking_lot.exceptions import NoVehicleParked, ParkingSpotAlreadyOccupied


class ParkingSpot(metaclass=ABCMeta):
    
    @property
    @abstractmethod
    def __spot_type__(self) -> str:
        pass
    
    @property
    @abstractmethod
    def occupied(self) -> bool:
        pass

    @property
    @abstractmethod
    def cost_per_second(self) -> int:
        pass

    @property
    @abstractmethod
    def parking_spot_id(self) -> int:
        pass

    @property
    @abstractmethod
    def parked_vehicle(self) -> Vehicle:
        pass
    
    def park(self, vehicle: Vehicle):
        if self.occupied:
            raise ParkingSpotAlreadyOccupied
        self.parked_vehicle = vehicle
        self.occupied = True

    def unpark(self):
        if not self.occupied:
            raise NoVehicleParked
        self.parked_vehicle = None
        self.occupied = False


class BikeParkingSpot(ParkingSpot):
    __spot_type__ = "Bike"

    occupied = False
    parked_vehicle = None
    cost_per_second = 1
    parking_spot_id = None

    def __init__(self, parking_spot_id):
        self.parking_spot_id = parking_spot_id


class CarParkingSpot(ParkingSpot):
    __spot_type__ = "Car"

    occupied = False
    parked_vehicle = None
    cost_per_second = 2
    parking_spot_id = None

    def __init__(self, parking_spot_id):
        self.parking_spot_id = parking_spot_id


class TruckParkingSpot(ParkingSpot):
    __spot_type__ = "Truck"

    occupied = False
    parked_vehicle = None
    cost_per_second = 5
    parking_spot_id = None

    def __init__(self, parking_spot_id):
        self.parking_spot_id = parking_spot_id
