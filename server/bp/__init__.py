from . import auth


def init_bp(app):
    app.register_blueprint(auth.bp)

