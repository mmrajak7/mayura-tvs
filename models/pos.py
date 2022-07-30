from flask_login import UserMixin
from sqlalchemy import Date

from app import db


class Pos(db.Model, UserMixin):
    pos_no = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    tran_date = db.Column(Date, nullable=False)
    batch_no = db.Column(db.String(length=100), nullable=False)
    card_type = db.Column(db.String(length=100), nullable=False)
    ti = db.Column(db.String(length=100), nullable=True)
    card_no = db.Column(db.String(length=100), nullable=True)
    approve_code = db.Column(db.String(length=100), nullable=True)
    gross_amt = db.Column(db.String(length=100), nullable=True)
    mdr = db.Column(db.String(length=100), nullable=True)
    gst = db.Column(db.String(length=100), nullable=True)
    net_amount = db.Column(db.String(length=100), nullable=True)
    process_date = db.Column(db.String(length=100), nullable=True)
    frame_no = db.Column(db.String(length=100), nullable=True)

    def to_dict(self):
        return {
            'pos_no': self.pos_no,
            'tran_date': self.tran_date and self.tran_date.strftime("%m/%d/%Y"),
            'batch_no': self.batch_no,
            'card_type': self.card_type,
            'ti': self.ti,
            'card_no': self.card_no,
            'approve_code': self.approve_code,
            'gross_amt': self.gross_amt,
            'mdr': self.mdr,
            'gst': self.gst,
            'net_amount': self.net_amount,
            'process_date': self.process_date,
            'frame_no': self.frame_no
        }
