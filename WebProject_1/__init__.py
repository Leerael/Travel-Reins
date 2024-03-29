"""
The flask application package.
"""

from flask import Flask
from WebProject_1.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login = LoginManager(app)
login.init_app(app)
login.login_view = 'login'

from WebProject_1 import views, models

db.init_app(app)

