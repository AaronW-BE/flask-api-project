# file for auth blueprint
import time
import functools

from flask import (
    Blueprint, flash, request, jsonify
)

from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import get_jwt

from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=['GET'])
def register():
    return {
        "data": "ok"
    }


@bp.route('/login', methods=['POST'])
def login():
    json = request.get_json()
    username = json['username']
    password = json['password']

    if username != "admin" or password != "admin":
        return jsonify({
            "msg": "用户名或密码错误",
        })

    user = {"id": 1, "username": "admin"}
    tmp = time.time()
    additional_claims = {"timestamp": tmp, "expire_in": 7200}
    access_token = create_access_token(identity=user, additional_claims=additional_claims)
    return jsonify({
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
