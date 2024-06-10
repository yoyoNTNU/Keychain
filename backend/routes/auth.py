from flask import Blueprint, request, jsonify
from services.auth_service import register_user

auth_routes = Blueprint('auth', __name__)

@auth_routes.route('/register', methods=['POST'])
def register():
    if request.content_type != 'application/x-www-form-urlencoded':
        return jsonify({'error': 'Unsupported Media Type, must be application/x-www-form-urlencoded'}), 415
    data = request.form
    response, status_code = register_user(data)
    return jsonify(response), status_code

@auth_routes.route('/bind_google', methods=['PATCH'])
def bind_google():
    data = request.json
    user_id = data.get('user_id')
    google_id = data.get('google_id')
    
    user = User.query.get(user_id)
    if user:
        user.google_id = google_id
        db.session.commit()
        return jsonify({'message': 'Google account linked successfully'}), 200
    return jsonify({'error': 'User not found'}), 404

@auth_routes.route('/bind_apple', methods=['PATCH'])
def bind_apple():
    data = request.json
    user_id = data.get('user_id')
    apple_id = data.get('apple_id')
    
    user = User.query.get(user_id)
    if user:
        user.apple_id = apple_id
        db.session.commit()
        return jsonify({'message': 'Apple account linked successfully'}), 200
    return jsonify({'error': 'User not found'}), 404

@auth_routes.route('/')
@auth_routes.route('/login', methods=['POST'])
def login():
    print("login")
    return jsonify({'message': 'login successfully'})