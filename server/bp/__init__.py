from . import auth, user


def init_bp(app):
    app.register_blueprint(auth.bp)
    # app.register_blueprint(user.bp)

