import pymysql

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from api import settings
from api.extensions import db, migrate
from api.redis.clients import RedisClient


def create_app():
    pymysql.install_as_MySQLdb()

    app = Flask(__name__)
    CORS(app)

    from api.data.models import Item

    app.config["SQLALCHEMY_DATABASE_URI"] = app.config["SQLALCHEMY_DATABASE_URI"] = settings.DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    try:
        r_c = RedisClient()
        r_c._redis.ping()
    except Exception as e:
        raise Exception(f"Redis connection failed: {e}")

    db.init_app(app)
    migrate.init_app(app, db)

    return app
