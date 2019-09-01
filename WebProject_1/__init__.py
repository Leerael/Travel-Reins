"""
The flask application package.
"""

from flask import Flask
from WebProject_1.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
db.init_app(app)
migrate = Migrate(app, db)

login = LoginManager(app)
login.init_app(app)
login.login_view = 'login'

Bootstrap(app)

from WebProject_1 import views, models

from .templates.admin import admin as admin_blueprint
app.register_blueprint(admin_blueprint, url_prefix='/admin')

from .templates.auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

from .templates.home import home as home_blueprint
app.register_blueprint(home_blueprint)

from .templates.user import user as user_blueprint
app.register_blueprint(user_blueprint)

