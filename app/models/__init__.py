from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .category import Category
from .menu import Menu
from .customer import Customer
from .order import Order