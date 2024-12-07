from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

from .customer import Customer
from .customer_account import CustomerAccount
from .product import Product
from .order import Order
