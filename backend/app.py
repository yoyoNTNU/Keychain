from flask import Flask

app = Flask(__name__)

app.config.from_pyfile('config.py')

from routes.auth import auth_routes
from routes.password import password_routes

app.register_blueprint(auth_routes)
app.register_blueprint(password_routes)

if __name__ == '__main__':
    app.run(debug=True)
