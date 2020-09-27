from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_seeder import FlaskSeeder
from flask_marshmallow import Marshmallow
app=Flask(__name__)
app.config.from_object(Config)
db=SQLAlchemy(app)
marshmallow=Marshmallow(app)
migrate=Migrate(app,db)
login=LoginManager(app)
seeder=FlaskSeeder()
seeder.init_app(app,db)

login.login_view='login'

from app import routes,models

