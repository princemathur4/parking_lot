import time
from parking_lot.entities.vehicle import Car
from parking_lot.controller import ParkingManager


new_car_1 = Car()
parking_manager = ParkingManager()
parking_manager.show_parking_lot()
result_car_1 = parking_manager.enter(vehicle=new_car_1)
parking_manager.show_parking_lot()
ticket_car_1 = result_car_1["data"]

new_car_2 = Car()
result_car_2 = parking_manager.enter(vehicle=new_car_2)
parking_manager.show_parking_lot()
ticket_car_2 = result_car_2["data"]
time.sleep(3)

parking_manager.exit(parking_ticket=ticket_car_1)
parking_manager.show_parking_lot()

time.sleep(2)
parking_manager.exit(parking_ticket=ticket_car_2)
parking_manager.show_parking_lot()