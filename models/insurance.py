from flask_login import UserMixin
from sqlalchemy import Date

from app import db


class Insurance(db.Model, UserMixin):
    insurance_no = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    date = db.Column(Date, nullable=False)
    customer_name = db.Column(db.String(length=100), nullable=False)
    vehicle = db.Column(db.String(length=100), nullable=False)
    type = db.Column(db.String(length=100), nullable=True)
    policy_company = db.Column(db.String(length=100), nullable=True)
    chasis_no = db.Column(db.String(length=100), nullable=True)
    policy_no = db.Column(db.String(length=100), nullable=True)
    amount = db.Column(db.String(length=100), nullable=True)

    def to_dict(self):
        return {
            'insurance_no': self.insurance_no,
            'date': self.date,
            'customer_name': self.customer_name,
            'vehicle': self.vehicle,
            'type': self.type,
            'policy_company': self.policy_company,
            'chasis_no': self.chasis_no,
            'policy_no': self.policy_no,
            'amount': self.amount
        }
