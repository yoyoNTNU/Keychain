from flask import Blueprint, request, jsonify
password_routes = Blueprint('passwords', __name__)

@password_routes.route('/passwords', methods=['GET'])
def get_passwords():
    print("get pwd")
    passwords = []  
    return jsonify(passwords)

@password_routes.route('/passwords', methods=['POST'])
def save_password():
    print("save pwd")
    return jsonify({'message': 'Password saved successfully'})

@password_routes.route('/passwords/<int:id>', methods=['PATCH'])
def update_password(id):
    print("update pwd")
    return jsonify({'message': 'Password updated successfully'})

@password_routes.route('/passwords/<int:id>', methods=['DELETE'])
def delete_password(id):
    print("delete pwd")
    return jsonify({'message': 'Password deleted successfully'})
