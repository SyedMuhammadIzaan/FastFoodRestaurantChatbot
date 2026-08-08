from datetime import datetime
from app.models import db

class Category(db.Model):
    __tablename__="category"

    id=db.Column(db.Integer,nullable=False,primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    created_at=db.Column(db.DateTime,default=datetime.utcnow)

    db.relationship("Menu",backref=db.backref('category',lazy=True))

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'created_at': self.created_at
        }