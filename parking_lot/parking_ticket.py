from datetime import datetime
from parking_lot.entities.vehicle import Vehicle
from parking_lot.entities.parking_spot import ParkingSpot


class ParkingTicket:
    parking_spot_id: int
    time_of_entry: datetime

    def __init__(self, parking_spot_id):
        self.parking_spot_id = parking_spot_id
        self.time_of_entry = datetime.now()
