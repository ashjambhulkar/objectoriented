from enum import Enum


class AccountStatus(Enum):
  ACTIVE, BLACKLISTED, CANCELLED, PENDING, UNKNOWN = 1, 2, 3, 4, 5


class OrderStatus(Enum):
  ACTIVE, CANCELLED, PENDING, SHIPPED, COMPLETED, REFUNDAPPLIED = 1, 2, 3, 4, 5, 6


class PayementStatus(Enum):
  PAID, FAILED, COMPLETED, FILLED, DECLINED, ABANDONED, REFUNDED = 1, 2, 3, 4, 5, 6, 7


class ShipmentStatus(Enum):
  DELIVERED, INITIATED, FAILED, RETURN, CANCELLED, HOLD, UNKNOWN = 1, 2, 3, 4, 5, 6, 7


class Address:
  def __init__(self, house_number, street_name, city, state, country):
    self.house_number = house_number
    self.street_name = street_name
    self.city = city
    self.state = state
    self.country = country

  
class Account:
  def __init__(self, username, email, password, phone, shipping_address, status=AccountStatus.ACTIVE):
    self.username = username
    self.email = email
    self.password = password
    self.phone = phone
    self.shipping_address = shipping_address
    self.status = status

  
  def reset_password(self, new_password):
    pass

  def edit_account_details(self):
    pass

from abc import ABC, abstractmethod

class Customer(ABC):
  def __init__(self, cart, order):
    self.cart = cart
    self.order = order

  def get_cart(self):
    return self.cart

  def add_item_to_cart(self, item):
    pass

  def remove_item_from_cart(self, item):
    pass


class Guest(Customer):
  def create_account(self):
    pass

class Member(Customer):
  def __init__(self, id):
    self.id = id

  def place_order(self, order):
    pass


class Product(ABC):
  def __init__(self, name, weight, price, dimension, category, description, seller):
    self.name = name
    self.weight = weight
    self.price = price
    self.dimension = dimension
    self.category = category
    self.description = description
    self.seller = seller

  def add_product(self, name):
    pass

  def update_price(self, name, price):
    pass

  def get_available_count(self, name):
    return self.name.count()


class ProuductCategory:
  def __init__(self, name, description):
    self.name = name
    self.description = description


  def add_product_category(self, name):
    pass

  def edit_product_category(self, name):
    pass

  def remove_product_category(self, name):
    pass


class ProductReview:
  def __init__(self, rating, review, reviewer):
    self.rating = rating
    self.review = review
    self.reviewer = reviewer

class ShoppingCart:
  