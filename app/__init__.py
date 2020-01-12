from flask import Flask
from config import Config
from app.models import db
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
login = LoginManager(app)
login.login_view = 'login'

from app import routes
