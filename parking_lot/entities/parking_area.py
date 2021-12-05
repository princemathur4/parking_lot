from parking_lot.entities.vehicle import Vehicle
from parking_lot.exceptions import ParkingSpotNotAvailable, InvalidPaymentMethod, ParkingSpotAlreadyOccupied, \
    InvalidParkingSpotId
from parking_lot.entities.parking_spot import ParkingSpot


class ParkingArea:

    def __init__(self):
        self.parking_spots_per_vehicle_type = 2
        self.parking_space = {
            parking_spot_cls.__spot_type__: [
                parking_spot_cls((self.parking_spots_per_vehicle_type * idx) + (i + 1))
                for i in range(self.parking_spots_per_vehicle_type)
            ] for idx, parking_spot_cls in enumerate(ParkingSpot.__subclasses__())
        }

    def __str__(self):
        """
        This function will return the string representation of the Parking Area
        :return:
        """
        result = []
        for spot_type in self.parking_space:
            result.append(f"\n{'_' * 11}" + ''.join([f"{'_' * 5}_" for i in range(self.parking_spots_per_vehicle_type)]) + "\n")
            result.append(f"{spot_type}s:".ljust(10, ' '))
            for parking_spot in self.parking_space[spot_type]:
                result.append(str(parking_spot.parking_spot_id).ljust(5, ' '))
            result.append(f"\n|{' '*10}")
            for parking_spot in self.parking_space[spot_type]:
                result.append("XXXXX" if parking_spot.occupied else "     ")
            result.extend([f"\n|{'_'*10}", *[f"{'_' * 5}" for i in range(self.parking_spots_per_vehicle_type)]])
        return "PARKING ---------->" + ("|".join(result)) + "|\n"

    def get_free_parking_spot_id(self, vehicle_type):
        for parking_spot in self.parking_space[vehicle_type]:
            if not parking_spot.occupied:
                return parking_spot.parking_spot_id
        raise ParkingSpotNotAvailable

    def assign_parking_spot(self, parking_spot_id: ParkingSpot.parking_spot_id, vehicle: Vehicle):
        for parking_spot in self.parking_space[vehicle.__vehicle_type__]:
            if parking_spot.parking_spot_id == parking_spot_id:
                parking_spot.park(vehicle)

    def get_parking_spot_fees_by_id(self, parking_spot_id: ParkingSpot.parking_spot_id):
        for vehicle_type in self.parking_space.keys():
            for parking_spot in self.parking_space[vehicle_type]:
                if parking_spot.parking_spot_id == parking_spot_id:
                    return parking_spot.cost_per_second
        raise InvalidParkingSpotId

    def unassign_parking_spot(self, parking_spot_id: ParkingSpot.parking_spot_id):
        for vehicle_type in self.parking_space.keys():
            for parking_spot in self.parking_space[vehicle_type]:
                if parking_spot.parking_spot_id == parking_spot_id:
                    parking_spot.unpark()
