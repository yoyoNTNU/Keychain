from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import Config


app = Flask(__name__)

app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from routes.auth import auth_routes
from routes.password import password_routes
from models.user import User
from models.password import Password

app.register_blueprint(auth_routes)
app.register_blueprint(password_routes)

if __name__ == '__main__':
    app.run(debug=True)
