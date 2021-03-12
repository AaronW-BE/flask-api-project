import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from . import resources, bp

db = SQLAlchemy()


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="myapp",
        SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:123456@121.43.160.6:3306/flask-api',
        SQLALCHEMY_TRACK_MODIFICATIONS=True
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)

    bp.init_bp(app)

    resources.init_resources(app)

    @app.route("/hello")
    def hello():
        return 'Hello world'

    return app

