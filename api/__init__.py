import pymysql

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


from api import settings
from api.flask_extenstions import db, migrate


def create_app():
    pymysql.install_as_MySQLdb()

    app = Flask(__name__)
    CORS(app)

    from api.data.models import Item

    app.config["SQLALCHEMY_DATABASE_URI"] = app.config["SQLALCHEMY_DATABASE_URI"] = settings.DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    migrate.init_app(app, db)

    return app
