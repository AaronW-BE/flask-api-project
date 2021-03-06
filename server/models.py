import datetime

from werkzeug.security import generate_password_hash

from server import db, jwt, ma

user_roles = db.Table(
    "user_roles",
    db.Column("role_id", db.Integer, db.ForeignKey("role.id"), primary_key=True),
    db.Column("user_id", db.Integer, db.ForeignKey("user.id"), primary_key=True)
)

user_departments = db.Table(
    "user_departments",
    db.Column("department_id", db.Integer, db.ForeignKey("department.id"), primary_key=True),
    db.Column("user_id", db.Integer, db.ForeignKey("user.id"), primary_key=True)
)

role_permissions = db.Table(
    "role_permissions",
    db.Column("role_id", db.Integer, db.ForeignKey("role.id"), primary_key=True),
    db.Column("permission_id", db.Integer, db.ForeignKey("permission.id"), primary_key=True)
)


user_permissions = db.Table(
    "user_permissions",
    db.Column("user_id", db.Integer, db.ForeignKey("user.id"), primary_key=True),
    db.Column("permission_id", db.Integer, db.ForeignKey("permission.id"), primary_key=True)
)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, nullable=False)
    phone = db.Column(db.String(16), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    create_at = db.Column(db.DateTime, default=datetime.datetime.now())

    profile = db.relationship("Profile", uselist=False, backref='user', lazy=True)
    roles = db.relationship("Role", secondary=user_roles, backref=db.backref("users", lazy="dynamic"))

    def __init__(self, username, password, phone=""):
        self.username = username
        self.phone = phone
        self.password = generate_password_hash(password)
        self.create_at = datetime.datetime.now()


@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return User.query.filter_by(id=identity).one_or_none()


class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), default="")
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False, comment="?????????")


class Permission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False, comment="?????????")


class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False, comment="????????????")


class Audit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sn = db.Column(db.String(32), unique=True, comment="?????????")


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        fields = ("username", "id", "create_at", "last_login_at")


class ProfileSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Profile


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(32), unique=True)
    title = db.Column(db.String(64))
    price = db.Column(db.Float)
    express = db.Column(db.String(64))


class BookSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Book
