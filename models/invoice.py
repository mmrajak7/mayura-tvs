from app import db, login_manager
from sqlalchemy import DateTime
from datetime import datetime
from flask_login import UserMixin

from models.user import User


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Invoice(db.Model, UserMixin):
    accessories_cost = db.Column(db.String(length=60), nullable=False)
    affidavit_cost = db.Column(db.String(length=60), nullable=False)
    booking_no = db.Column(db.Integer())
    comments = db.Column(db.String(length=250), nullable=False)
    creation_date = db.Column(DateTime, default=datetime.now)
    discount = db.Column(db.String(length=60), nullable=False)
    fancy_number_cost = db.Column(db.String(length=60), nullable=False)
    finance_margin = db.Column(db.String(length=60), nullable=False)
    GST = db.Column(db.String(length=60), nullable=False)
    handling_cost = db.Column(db.String(length=60), nullable=False)
    insurance_cost = db.Column(db.String(length=60), nullable=False)
    payment_no = db.Column(db.Integer(), primary_key=True)
    invoice_path = db.Column(db.String(length=250), nullable=False)
    last_update_date = db.column(DateTime, default=datetime.now, onupdate=datetime.now)
    mode_of_payment = db.Column(db.String(length=60), nullable=False)
    pos_fee = db.Column(db.String(length=100), nullable=False, unique=True)
    rto_free = db.Column(db.String(length=100), nullable=False)
    vehicle_price = db.Column(db.String(length=50), nullable=False)

    def __repr__(self):
        return f'<Invoice: {self.payment_no}>. Booking : {self.booking_no}'
