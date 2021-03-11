from . import db

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

    profile = db.relationship("Profile", backref='address', lazy=True)
    permissions = db.relationship("Permission", secondary=user_permissions, lazy="subquery",
                                  backref=db.backref("roles", lazy=True))

    def __repr__(self):
        return '<User %r>' % self.username


class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), default="")
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False, comment="角色名")
    permissions = db.relationship("Permission", secondary=user_roles, lazy="subquery",
                                  backref=db.backref("roles", lazy=True))


class Permission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False, comment="权限名")


class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False, comment="部门名称")


class Audit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sn = db.Column(db.String(32), unique=True, comment="流水号")

