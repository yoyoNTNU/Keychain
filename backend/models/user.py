from app import db
from datetime import datetime
import pytz

tz = pytz.timezone('Asia/Taipei')

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(256), nullable=False)
    google_id = db.Column(db.String(100), nullable=True)
    apple_id = db.Column(db.String(100), nullable=True)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(tz))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(tz), onupdate=lambda: datetime.now(tz))

    passwords = db.relationship('Password', back_populates='user')

    def __repr__(self):
        return f'<User {self.username}>'
