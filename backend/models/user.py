from app import db
from datetime import datetime
import pytz
from sqlalchemy.schema import UniqueConstraint


tz = pytz.timezone('Asia/Taipei')

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=True)
    password = db.Column(db.String(256), nullable=True)
    google_id = db.Column(db.String(100), nullable=True)
    apple_id = db.Column(db.String(100), nullable=True)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(tz))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(tz), onupdate=lambda: datetime.now(tz))

    passwords = db.relationship('Password', back_populates='user')

    __table_args__ = (
        db.UniqueConstraint('username', name='uq_username'),
        db.UniqueConstraint('google_id', name='uq_google_id'),
        db.UniqueConstraint('apple_id', name='uq_apple_id'),
    )


    def __repr__(self):
        return f'<User {self.username}>'
