from datetime import datetime
from app.models import db

class Customer(db.Model):
    __tablename__ = 'customer'

    id=db.Column(db.Integer,nullable=False,primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    email=db.Column(db.String(100),nullable=False,unique=True)
    phone=db.Column(db.String(15),nullable=False,unique=True)
    created_at=db.Column(db.DateTime,default=datetime.utcnow)

    db.relationship("Order",backref=db.backref('customer',lazy=True))

    def to_dict(self):
       return {
           'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'created_at': self.created_at
        }