from app import db, login_manager
from sqlalchemy import DateTime
from datetime import datetime
from flask_login import UserMixin

from models.user import User


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Exchange_vehicle(db.Model, UserMixin):
    comments = db.Column(db.String(length=250), nullable=False)
    cost = db.Column(db.String(length=100), nullable=False)
    creation_date = db.Column(DateTime, default=datetime.now)
    delivery_chellan_no = db.Column(db.String(length=50), nullable=False)
    description = db.Column(db.String(length=100), nullable=False)
    documents_received = db.Column(db.String(length=100), nullable=False)
    engine_no = db.Column(db.String(length=100), nullable=False, unique=True)
    frame_no = db.Column(db.Integer(), primary_key=True)
    last_update_date = db.column(DateTime, default=datetime.now, onupdate=datetime.now)
    model = db.Column(db.String(length=60), nullable=False)
    resale_dealer = db.Column(db.String(length=100), nullable=False)
    vehicle_type = db.Column(db.String(length=60), nullable=False)

    def __repr__(self):
        return f'<Exchange_vehicle: {self.frame_no}>'
