from app import db
from sqlalchemy import DateTime
from flask_login import UserMixin


class Booking(db.Model, UserMixin):
    booking_no = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    accessories = db.Column(db.String(length=100), nullable=True)
    booking_date = db.Column(DateTime, nullable=False)
    delivery_chellan_no = db.Column(db.String(length=50), nullable=True)
    delivery_date = db.Column(DateTime, nullable=True)
    dealer = db.Column(db.String(length=100), nullable=True)
    description = db.Column(db.String(length=100), nullable=True)
    exchange_vehicle_frame_no = db.Column(db.Integer(), nullable=True)
    frame_no = db.Column(db.Integer(), db.ForeignKey('vehicle.frame_no'), nullable=False)
    customer_no = db.Column(db.Integer(), db.ForeignKey('customer.customer_no'), nullable=False)
    vehicle_type = db.Column(db.String(length=60), nullable=False)
    comments = db.Column(db.String(length=250), nullable=True)
    GST = db.Column(db.String(length=60), nullable=True)
    helmet = db.Column(db.String(length=60), nullable=True)
    invoice_no = db.Column(db.String(length=60), nullable=True)
    model = db.Column(db.String(length=60), nullable=False)
    rc_issue_date = db.Column(DateTime, nullable=True)
    status = db.Column(db.String(length=60), nullable=False)
    tools = db.Column(db.String(length=60), nullable=True)
    vehicle_registration_no = db.Column(db.String(length=60), nullable=True)
    last_updated_by = db.Column(db.String(length=100))
    registration_date = db.Column(DateTime, nullable=True)

    def __repr__(self):
        return f'<Booking: {self.booking_no}>'

    def to_dict(self):
        return {
            'booking_no': self.booking_no,
            'accessories': self.accessories,
            'booking_date': self.booking_date.strftime("%m/%d/%Y"),
            'delivery_chellan_no': self.delivery_chellan_no,
            'delivery_date': self.delivery_date and self.delivery_date.strftime("%m/%d/%Y"),
            'description': self.description,
            'exchange_vehicle_frame_no': self.exchange_vehicle_frame_no,
            'frame_no': self.frame_no,
            'customer_no': self.customer_no,
            'vehicle_type': self.vehicle_type,
            'comments': self.comments,
            'GST': self.GST,
            'helmet': self.helmet,
            'invoice_no': self.invoice_no,
            'rc_issue_date': self.rc_issue_date and self.rc_issue_date.strftime("%m/%d/%Y"),
            'model': self.model,
            'status': self.status,
            'tools': self.tools,
            'vehicle_registration_no': self.vehicle_registration_no,
            'dealer': self.dealer,
            'registration_date': self.registration_date and self.registration_date.strftime("%m/%d/%Y")
        }
