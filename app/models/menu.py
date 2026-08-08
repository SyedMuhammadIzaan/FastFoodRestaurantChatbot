from datetime import datetime
from app.models import db

class Menu(db.Model):
    __tablename__ = 'menu'

    id=db.Column(db.Integer,nullable=False,primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    description=db.Column(db.String(100),nullable=False)
    deliveryTime=db.Column(db.String(100),nullable=False)
    price=db.Column(db.Float,nullable=False)
    categoryId=db.Column(db.Integer,db.ForeignKey('category.id'),nullable=False)
    created_at=db.Column(db.DateTime,default=datetime.utcnow)

    category=db.relationship("Category",backref=db.backref('menu',lazy=True))

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'categoryId': self.categoryId,
            'categoryName':self.category.name if self.category else None,
            'created_at': self.created_at
        }


