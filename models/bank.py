from flask_login import UserMixin
from sqlalchemy import Date

from app import db


class Bank(db.Model, UserMixin):
    bank_no = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    tran_date = db.Column(Date, nullable=False)
    value_date = db.Column(Date, nullable=False)
    chq_no = db.Column(db.String(length=100), nullable=False)
    transaction_particulars = db.Column(db.String(length=100), nullable=True)
    amount = db.Column(db.String(length=100), nullable=True)
    dr_cr = db.Column(db.String(length=100), nullable=True)
    balance = db.Column(db.String(length=100), nullable=True)
    branch_name = db.Column(db.String(length=100), nullable=True)
    comments = db.Column(db.String(length=100), nullable=True)
    marker = db.Column(db.String(length=100), nullable=True)

    def to_dict(self):
        return {
            'bank_no': self.bank_no,
            'tran_date': self.tran_date,
            'value_date': self.value_date and self.value_date.strftime("%m/%d/%Y"),
            'chq_no': self.chq_no,
            'transaction_particulars': self.transaction_particulars,
            'amount': self.amount,
            'dr_cr': self.dr_cr,
            'balance': self.balance,
            'branch_name': self.branch_name,
            'comments': self.comments,
            'marker': self.marker
        }
