from flask_login import UserMixin

from app import db, login_manager
from models.user import User


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Vehicle(db.Model, UserMixin):
    frame_no = db.Column(db.Integer(), primary_key=True, nullable=False)
    engine_no = db.Column(db.String(length=100), nullable=False, unique=True)
    dealer = db.Column(db.String(length=100), nullable=False)
    delivery_chellan_no = db.Column(db.String(length=50), nullable=True)
    description = db.Column(db.String(length=100), nullable=True)
    model = db.Column(db.String(length=60), nullable=False)
    vehicle_type = db.Column(db.String(length=60), nullable=False)
    comments = db.Column(db.String(length=250), nullable=True)
    GST = db.Column(db.String(length=60), nullable=True)
    status = db.Column(db.String(length=60), nullable=False)

    def __repr__(self):
        return f'<Vehicle: {self.frame_no}>'

    def to_dict(self):
        return {
            'frame_no': self.frame_no,
            'engine_no': self.engine_no,
            'dealer': self.dealer,
            'delivery_chellan_no': self.delivery_chellan_no,
            'description': self.description,
            'model': self.model,
            'vehicle_type': self.vehicle_type,
            'comments': self.comments,
            'GST': self.GST,
            'status': self.status
        }

    def as_dict(self):
        value = str(self.frame_no) + "-" + self.model + "-" + self.dealer
        return {
            'value': value,
            'text': value
        }
