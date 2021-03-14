from server.utils.response import resp_success
from flask import (
    Blueprint, flash, request, jsonify
)

bp = Blueprint('user', __name__, url_prefix='/user')


@bp.route('current-roles', methods=['GET'])
def get_login_user_roles():
    return resp_success({})


@bp.route('current-profile', method=['GET'])
def get_login_user_profile():
    return resp_success()
