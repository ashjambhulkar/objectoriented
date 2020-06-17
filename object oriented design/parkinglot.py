from enum import Enum
from abc import ABC, abstractmethod


class ParkingSpotType(Enum):
  Motorbike, Large, Compact, Electric, Handicapped = 1, 2, 3, 4, 5


class VehicleType(Enum):
  MotorBike, Car, Truck, Van = 1, 2, 3, 4


class AccountStatus(Enum):
  Active, Blacklisted, Cancelled, Hold = 1, 2, 3, 4


class ParkingTicketStatus(Enum):
  Active, Paid, Lost = 1, 2, 3


class Address:
  def __init__(self, street, street_name, city, state, country):
    self.stree_number = street
    self.stree_name = street_name
    self.city = city
    self.state = state
    self.country = country


class Person:
  def __init__(self, name, age , gender, email, phone_number):
    self.name = name
    self.age = age
    self.gender = gender
    self.email = email
    self.phone_number = phone_number 
    

class Account:
  def __init__(self, username, password, person, status=AccountStatus.Active):
    self.username = username
    self.password = password
    self.person = person
    self.status = status

  def reset_password(self):
    pass


class Admin(Account):
  def __init__(self, username,  password, person, status=AccountStatus.Active):
    super.__init__(username, password, person, status)

  def add_parking_floor(self, floor):
    pass

  def add_parking_spot(self, floor_name, spot):
    pass

  def add_parking_rate(self, rate):
    pass

  def modify_parking_rate(self, rate):
    pass

  def add_parking_attendant(self, person):
    pass

  def add_entrance_panel(self, entry):
    pass

  def add_exit_panel(self, exit):
    pass


class ParkingAttendant(Account):
  def __init__(self, username, password, person, status=AccountStatus.Active):
    super.__init__(username, password, person, status)

  def process_ticket(self, ticket_number):
    pass


class ParkingSpot(ABC):
  def __init__(self, number, parking_spot_type):
    self.number = number
    self.parking_spot_type = parking_spot_type
    self.free = True
    self.vehicle = None

  def is_free(self, number):
    return self.free

  def assign_vehicle(self, vehicle):
    self.vehicle = vehicle
    self.free = False

  def remove_vehicle(self):
    self.vehicle = None
    self.free = True

  
class HandicappedSpot(ParkingSpot):
  def __init__(self, number):
    super().__init__(number, ParkingSpotType.Handicapped)


class LargeSpot(ParkingSpot):
  def __init__(self, number):
    super().__init__(number, ParkingSpotType.Large)


class Vehicle(ABC):
  def __init__(self, vehicle_type, vehicle_number, ticket=None):
    self.vehicle_type = vehicle_type
    self.vehicle_number = vehicle_number
    self.ticket = ticket

  def assign_ticket(self, ticket):
    self.ticket = ticket


class Car(Vehicle):
  def __init__(self, vehicle_number, ticket=None):
    super().__init__(VehicleType.Car, vehicle_number, ticket)


class ParkingFloor:
  def __init__(self, name):
    self.name = name
    self.hadicapped_spots = {}
    self.compact_spots = {}
    self.motorbike_spots = {}
    self.display_board = ParkingDisplayBoard(id)

  def add_parking_spot(self, spot):
    pass

  def assign_vehicle_to_spot(self, vehicle):
    pass

  def update_display_board(self, spot):
    pass

  def free_parking_spot(self, spot):
    pass


class ParkingDisplayBoard():
  def __init__(self, id):
    self.id = id
    self.hadicapped_empty_spot = None
    self.car_empty_spot = None

  def show_empty_spot(self):
    if self.hadicapped_empty_spot.is_free():
      return "Spots are free"
    else:
      return "spots are not free"


    if self.car_empty_spot.is_free():
      return "Car spot is empty"
    else:
      return "Car spot is not empty"

import threading
class ParkingLot:
  instance = None
  class OnlyOne:
    def __init__(self, name, address):
      self.name = name
      self.address = address
      self.parking_rate = ParkingRate()
      self.car_spot_count = 0
      self.motorbike_spot_count = 0
      self.entry_panel = {}
      self.exit_panel = {}
      self.parking_floor = {}
      self.active_tickets = {}
      self.lock = threading.Lock()

  def __init__(self, name, address):
    if not ParkingLot.instance:
      ParkingLot.instance = ParkingLot.OnlyOne(name, address)
    else:
      ParkingLot.instance.name = name
      ParkingLot.instance.address = address

    def __getattr__(self, name):
      return getattr(self.instance, name)

    def get_new_parking_ticket(self, vehicle):
      if self.isfull(vehicle.get_type()):
        raise Exception("Parking is full")
      
      self.lock.aquire()
      ticket = ParkingTicket()
      vehicle.assign_ticket(ticket)
      ticket.save_to_db()

      self.increment_spot_count(vehicle.get_type())
      self.active_ticket.put(ticket.get_ticket_number(), ticket)
      self.lock.release()
      return ticket
  
  def add_parking_floor(self):
    pass

  def add_entrance_panel(self):
    pass

  def add_exit_panel(self):
    pass