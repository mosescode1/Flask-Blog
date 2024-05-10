

from flask_login import LoginManager
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///usersite.db'
app.config['SECRET_KEY'] = '139e092bf613eb663af7740aa4308cca'

bycrypt = Bcrypt(app)


class Base(DeclarativeBase):
    #    from flaskblog import route
    pass


db = SQLAlchemy(model_class=Base)
db.init_app(app)
login_manager = LoginManager(app)


class fixImportationError():
    from flaskblog import route
# thid is to avoid circular import
