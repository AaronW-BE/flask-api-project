# file for auth blueprint
import time
import functools

from flask import (
    Blueprint, flash, request, jsonify
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

    if username != "admin" and check_password_hash(
            'pbkdf2:sha256:150000$rTmH4uCz$92fefb2c4fb448bbf8d553d93ac8b79f1c5148b9138a46e8e9e01c3b5825187b',
            password) is not True:
        return resp_fail("用户名或密码错误")

    user = {"id": 1, "username": "admin"}
    tmp = time.time()
    additional_claims = {"timestamp": tmp, "expire_in": 7200}
    access_token = create_access_token(identity=user, additional_claims=additional_claims)
    return resp_success({
        "access_token": access_token, "timestamp": int(tmp), "expire_in": 7200
    })


@bp.route('/current', methods=['GET'])
# @jwt_required()
def current():
    claims = get_jwt()
    current_user = get_jwt_identity()
    return jsonify(current_user=current_user)


@bp.route('/logout', methods=['POST'])
def logout():
    jti = get_jwt()["jti"]
