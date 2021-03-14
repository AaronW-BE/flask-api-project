import os

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

from flask_jwt_extended import verify_jwt_in_request
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
jwt = JWTManager()

jwt_excluded_paths = ["/auth/login", "/auth/register", "/healthy", "/favicon.ico"]


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="myapp",
        JWT_SECRET_KEY="myapp",
        JWT_ACCESS_TOKEN_EXPIRES=7200,
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

    jwt = JWTManager(app)

    from . import resources, bp
    db.init_app(app)
    bp.init_bp(app)

    resources.init_resources(app)

    @app.before_request
    def before_request():
        if request.path in jwt_excluded_paths:
            print("jwt validate ignored for [%s]" % request.path)
        else:
            print("jwt validate for [%s]" % request.path)
            verify_jwt_in_request()

    @app.route("/healthy")
    def healthy():
        return 'health'

    return app


