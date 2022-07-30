from flask_login import UserMixin
from sqlalchemy import Date

from app import db


class Cashbook(db.Model, UserMixin):
    cashbook_no = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    cashbook_date = db.Column(Date, nullable=False)
    nature_of_expenses = db.Column(db.String(length=100), nullable=False)
    details = db.Column(db.String(length=100), nullable=False)
    customer_name = db.Column(db.String(length=100), nullable=False)
    payments = db.Column(db.String(length=100), nullable=True)
    receipts = db.Column(db.String(length=100), nullable=True)
    closing_balance = db.Column(db.String(length=100), nullable=True)

    def to_dict(self):
        return {
            'cashbook_no': self.cashbook_no,
            'cashbook_date': self.cashbook_date and self.cashbook_date.strftime("%m/%d/%Y"),
            'nature_of_expenses': self.nature_of_expenses,
            'details': self.details,
            'customer_name': self.customer_name,
            'payments': self.payments,
            'receipts': self.receipts,
            'closing_balance': self.closing_balance
        }
