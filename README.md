// write your code here...

Q1: Design a parking lot

Parking Spot
- slot type
- slot number
- occupied: bool
- vehicle details
- vehicle entry datetime

PaymentSystem
payment methods - [Debit Card, Credit Card, Cash, UPI]

- do_payment

ParkingTicket
- parking spot id
- time of entry


Parking Lot
- Dedicated limited space = {
    "Car": [ParkingSpot1, ParkingSpot2, ParkingSpot3],
    "Bikes": [ParkingSpot1, ParkingSpot2, ParkingSpot3],
    "Trucks": [ParkingSpot1, ParkingSpot2, ParkingSpot3],
}
- vehicle queue - mapping - mapping -> vehicle details
- Number of vehicles present - mapping -> vehicle type and count
- Entry(vehicle_details)
    # do a check for parking space available or not
    # assign a parking space accordingly and
    # also update the details of vehicle in ParkingSpot
    # also generate a parkingTicket
    # else add in waiting in queue

- assign_parking_spot()

- Exit(parking_ticket)
    # we need to free the parking spot corresponding to that ticket
    # cost = calculate_cost(parking_ticket)
    # status = PaymentSystem.do_payment(cost)
    # perform a check if payment is successful or not
    # if there is any vehicle in queue waiting
    # then we need to assign a parking spot and do the payment accordingly
    Entry(first_vehicle_in_queue)

- calculate_cost(parking_ticket)
    multiply no of hours = current_time - parking_ticket.time
    vehicleobj = get_vehicle_obj(parking_ticket)
    return multiply no of hours * vehicleobj.parking_cost

Entities
Vehicle
Cars, Bikes, Trucks
1 - parking cost
2 - attributes for space/area that they occupy



tapaseid@gmail.com

