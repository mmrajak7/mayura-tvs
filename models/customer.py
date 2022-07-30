from app import db, login_manager
from sqlalchemy import DateTime
from datetime import datetime
from flask_login import UserMixin

from models.user import User


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Customer(db.Model, UserMixin):
    customer_no = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    customer_name = db.Column(db.String(length=50), nullable=False, unique=True)
    email = db.Column(db.String(length=50), nullable=True, unique=True)
    dob = db.Column(db.String(length=60), nullable=False)
    mobile1 = db.Column(db.String(length=60), nullable=False, unique=True)
    mobile2 = db.Column(db.String(length=60), nullable=True)
    mobile3 = db.Column(db.String(length=60), nullable=True)
    comment = db.Column(db.String(length=250), nullable=True)
    GST = db.Column(db.String(length=60), nullable=True)
    city = db.Column(db.String(length=60), nullable=True)
    street = db.Column(db.String(length=60), nullable=True)
    pincode = db.Column(db.String(length=60), nullable=True)
    # creation_date = db.Column(DateTime, default=datetime.now)

    # last_update_date = db.column(DateTime, default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return f'<Customer: {self.customer_no}>'

    def to_dict(self):
        return {
            'customer_no': self.customer_no,
            'customer_name': self.customer_name,
            'email': self.email,
            'dob': self.dob,
            'mobile1': self.mobile1,
            'mobile2': self.mobile2,
            'mobile3': self.mobile3,
            'comment': self.comment,
            'GST': self.GST,
            'city': self.city,
            'street': self.street,
            'pincode': self.pincode
        }

    def as_dict(self):
        return {
            'value': self.customer_no,
            'text': self.customer_name
        }
