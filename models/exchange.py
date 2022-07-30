from flask_login import UserMixin
from sqlalchemy import Date

from app import db


class Exchange(db.Model, UserMixin):
    exchange_no = db.Column(db.Integer(), primary_key=True)
    out_date = db.Column(Date, nullable=False)
    in_date = db.Column(Date, nullable=False)
    exchange_vehicle_name = db.Column(db.String(length=100), nullable=True)
    exchange_vehicle_value = db.Column(db.String(length=100), nullable=True)
    payment_status = db.Column(db.String(length=100), nullable=True)
    vehicle_name = db.Column(db.String(length=100), nullable=False)
    vehicle_type = db.Column(db.String(length=100), nullable=False)
    frame_no = db.Column(db.String(length=100), nullable=True)

    def to_dict(self):
        return {
            'exchange_no': self.exchange_no,
            'out_date': self.out_date and self.out_date.strftime("%m/%d/%Y"),
            'in_date': self.in_date,
            'exchange_vehicle_name': self.exchange_vehicle_name,
            'exchange_vehicle_value': self.exchange_vehicle_value,
            'payment_status': self.payment_status,
            'vehicle_name': self.vehicle_name,
            'vehicle_type': self.vehicle_type,
            'frame_no': self.frame_no
        }
