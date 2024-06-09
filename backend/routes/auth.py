from flask import Blueprint, request, jsonify
auth_routes = Blueprint('auth', __name__)

@auth_routes.route('/register', methods=['POST'])
def register():
    print("register")
    return jsonify({'message': 'register successfully'})

@auth_routes.route('/login', methods=['POST'])
def login():
    print("login")
    return jsonify({'message': 'login successfully'})