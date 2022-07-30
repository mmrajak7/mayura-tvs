from flask_login import UserMixin
from sqlalchemy import Date

from app import db


class Soa(db.Model, UserMixin):
    soa_no = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    date = db.Column(Date, nullable=False)
    dr_cr = db.Column(db.String(length=100), nullable=True)
    particulars = db.Column(db.String(length=100), nullable=True)
    reference = db.Column(db.String(length=100), nullable=True)
    vehicle_no = db.Column(db.String(length=100), nullable=False)
    vehicle_type = db.Column(db.String(length=100), nullable=False)
    debit = db.Column(db.String(length=100), nullable=True)
    credit = db.Column(db.String(length=100), nullable=True)
    frame_no = db.Column(db.String(length=100), nullable=True)
    cash_bank_finance = db.Column(db.String(length=100), nullable=True)
    ad_margin = db.Column(db.String(length=100), nullable=True)
    dealer = db.Column(db.String(length=100), nullable=True)

    def to_dict(self):
        return {
            'soa_no': self.soa_no,
            'date': self.date and self.date.strftime("%m/%d/%Y"),
            'dr_cr': self.dr_cr,
            'particulars': self.particulars,
            'reference': self.reference,
            'vehicle_no': self.vehicle_no,
            'vehicle_type': self.vehicle_type,
            'debit': self.debit,
            'credit': self.credit,
            'cash_bank_finance': self.cash_bank_finance,
            'ad_margin': self.ad_margin,
            'dealer': self.dealer
        }
