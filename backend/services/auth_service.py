from werkzeug.security import generate_password_hash
from models.user import User
from app import db

def register_user(data):
    username = data.get('username')
    password = data.get('password')
    google_id = data.get('google_id')
    apple_id = data.get('apple_id')

    if username and password:
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password=hashed_password)
    elif google_id:
        new_user = User(google_id=google_id)
    elif apple_id:
        new_user = User(apple_id=apple_id)
    else:
        return {'error': 'Invalid registration data'}, 400

    db.session.add(new_user)
    db.session.commit()

    return {'message': 'User registered successfully'}, 200
