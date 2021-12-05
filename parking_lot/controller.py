from datetime import datetime
from parking_lot.entities import Queue
from parking_lot.entities.parking_area import ParkingArea
from parking_lot.entities.payments import PaymentGateway
from parking_lot.entities.vehicle import Vehicle
from parking_lot.exceptions import ParkingSpotNotAvailable, InvalidPaymentMethod, ParkingSpotAlreadyOccupied, \
    InvalidParkingSpotId
from parking_lot.parking_ticket import ParkingTicket


class ParkingManager:

    def __init__(self):
        self.parking_area = ParkingArea()
        self.vehicle_waiting_queue = Queue()
        self.payment_gateway = PaymentGateway()

    def show_parking_lot(self):
        print(str(self.parking_area))

    def enter(self, vehicle: Vehicle):
        print(f"A {vehicle.__vehicle_type__} with number {vehicle.vehicle_registered_number} is in parking queue")
        try:
            free_parking_spot_id = self.parking_area.get_free_parking_spot_id(
                vehicle_type=vehicle.__vehicle_type__
            )
            new_parking_ticket = ParkingTicket(parking_spot_id=free_parking_spot_id)
            self.parking_area.assign_parking_spot(parking_spot_id=free_parking_spot_id, vehicle=vehicle)
            return {"status": True, "data": new_parking_ticket}
        except ParkingSpotNotAvailable:
            self.vehicle_waiting_queue.enqueue(vehicle)
            return {"status": False, "message":"Parking lot is full, please wait for sometime."}

    def exit(self, parking_ticket: ParkingTicket, payment_method="CASH"):
        total_parking_fees = self.calculate_parking_fees(parking_ticket=parking_ticket)
        print("Total parking fees: ₹", total_parking_fees)
        input("Press Enter to complete payment")
        self.payment_gateway.do_payment(total_amount=total_parking_fees, payment_method=payment_method)
        self.parking_area.unassign_parking_spot(parking_ticket.parking_spot_id)

        try:
            first_waiting_vehicle = self.vehicle_waiting_queue.peek()
            self.enter(first_waiting_vehicle)
        except Exception as e:
            pass

    def calculate_parking_fees(self, parking_ticket: ParkingTicket):
        total_parked_time = (datetime.now() - parking_ticket.time_of_entry).seconds
        cost_per_second = self.parking_area.get_parking_spot_fees_by_id(parking_ticket.parking_spot_id)
        print(f"Total parked time: {total_parked_time} seconds")
        return cost_per_second * total_parked_time
