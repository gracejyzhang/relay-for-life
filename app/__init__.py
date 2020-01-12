from flask import Flask
from config import Config
from flask_migrate import Migrate
from app.models import d
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = '95e01697dd1d1b4e543ae883d7fac988'
bcrypt = Bcrypt(app)
app.config.from_object(Config)
db.init_app(app)

from app import routes
