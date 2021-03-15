# file for auth blueprint
import time

from flask import (
    Blueprint, request, jsonify
)

from flask_jwt_extended import (create_access_token, get_jwt_identity, get_jwt)

from werkzeug.security import check_password_hash, generate_password_hash

from server.utils.response import resp_success, resp_fail
import server
import server.models

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=['POST'])
def register():
    json = request.get_json()
    username = json['username']
    password = json['password']

    user = server.models.User(username, password)

    server.db.session.add(user)
    server.db.session.commit()
    return resp_success("注册成功")


@bp.route('/login', methods=['POST'])
def login():
    json = request.get_json()
    username = json['username']
    password = json['password']

    user = server.models.User.query.filter_by(username=username).first()
    if user is None:
        return resp_fail("用户不存在")

    if not check_password_hash(user.password, password):
        return resp_fail("用户密码不正确")

    tmp = time.time()
    additional_claims = {"timestamp": tmp, "expire_in": 7200}
    access_token = create_access_token(identity={
        "id": user.id,
        "username": username,
    }, additional_claims=additional_claims)
    return resp_success({
        "token": access_token, "timestamp": int(tmp), "expire_in": 7200
    })


@bp.route('/current', methods=['GET'])
# @jwt_required()
def current():
    identity = get_jwt_identity()

    user = server.models.User.query.filter_by(id=identity.get("id")).first()
    user_schema = server.models.UserSchema()

    roles = user.roles

    profile_schema = server.models.ProfileSchema()
    profile = profile_schema.dump(user.profile)

    return jsonify(
        user=user_schema.dump(user),
        roles=roles,
        profile=profile
    )


@bp.route('/logout', methods=['POST'])
def logout():
    jti = get_jwt()["jti"]
    server.jwt_block_list.append(jti)
    return resp_success()

