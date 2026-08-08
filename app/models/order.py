from datetime import datetime
from app.models import db

class Order(db.Model):
    __tablename__ = 'order'

    id=db.Column(db.Integer,nullable=False,primary_key=True)
    customerId=db.Column(db.Integer,db.ForeignKey('customer.id'),nullable=False)
    menuId=db.Column(db.Integer,db.ForeignKey('menu.id'),nullable=False)
    quantity=db.Column(db.Integer,nullable=False)
    totalPrice=db.Column(db.Float,nullable=False)
    created_at=db.Column(db.DateTime,default=datetime.utcnow)

    db.relationship("Customer",backref=db.backref('order',lazy=True))

    def to_dict(self):
        return {
            'id': self.id,
            'menuId': self.menuId,
            'quantity': self.quantity,
            'totalPrice': self.totalPrice,
            'created_at': self.created_at
        }


class OrderMenu(db.Model):
    __tablename__ = 'order_menu'

    id=db.Column(db.Integer,nullable=False,primary_key=True)
    customerName=db.Column(db.String(100),nullable=False)
    phoneNo=db.Column(db.Integer,nullable=False)
    email=db.Column(db.String(250),unique=True,nullable=False)
    address=db.Column(db.String(250),nullable=False)
    city=db.Column(db.String(100),nullable=False)
    country=db.Column(db.String(100),nullable=False)
    itemName=db.Column(db.String(100),nullable=False)
    quantity=db.Column(db.Integer,nullable=False)
    totalPrice=db.Column(db.Float,nullable=False)
    status=db.Column(db.String(50),nullable=False,default='Pending')
    created_at=db.Column(db.DateTime,default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'customerName': self.customerName,
            'phoneNo': self.phoneNo,
            'email': self.email,
            'address': self.address,
            'city': self.city,
            'country': self.country,
            'itemName': self.itemName,
            'quantity': self.quantity,
            'totalPrice': self.totalPrice,
            'status': self.status,
            'created_at': self.created_at
        }