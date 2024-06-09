from flask import Blueprint
auth_routes = Blueprint('auth', __name__)

@auth_routes.route('/register', methods=['POST'])
def register():
    print("register")
    pass

@auth_routes.route('/login', methods=['POST'])
def login():
    print("login")
    pass