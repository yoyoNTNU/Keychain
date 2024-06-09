from app import db
from datetime import datetime
import pytz

tz = pytz.timezone('Asia/Taipei')

class Password(db.Model):
    __tablename__ = 'passwords'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    website_url = db.Column(db.String(200), nullable=False)
    website_name = db.Column(db.String(100), nullable=False)
    account = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(256), nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(tz))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(tz), onupdate=lambda: datetime.now(tz))

    user = db.relationship('User', back_populates='passwords')

    def __repr__(self):
        return f'<Password {self.website_name}>'
